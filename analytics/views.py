from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
from .models import PageVisit, ProductInteraction
from store.models import Inquiry

@staff_member_required
def analytics_dashboard(request):
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)
    
    # Context Data
    context = {}
    
    # 1. Total Visits (Weekly/Monthly)
    context['visits_week'] = PageVisit.objects.filter(timestamp__gte=week_ago).count()
    context['visits_month'] = PageVisit.objects.filter(timestamp__gte=month_ago).count()
    
    # 2. Product Views vs Inquiries (Conversion)
    # We can aggregate interactions by type
    interactions_week = ProductInteraction.objects.filter(timestamp__gte=week_ago).values('interaction_type').annotate(count=Count('id'))
    context['interactions_week'] = interactions_week
    
    # 3. Who enquired for which product (Top products by inquiry)
    top_enquired_products = Inquiry.objects.filter(created_at__gte=month_ago)\
        .values('product__name')\
        .annotate(total=Count('id'))\
        .order_by('-total')[:5]
    context['top_enquired_products'] = top_enquired_products
    
    # 4. Detailed recent enquiries
    context['recent_inquiries'] = Inquiry.objects.select_related('product').order_by('-created_at')[:10]
    
    return render(request, 'analytics/dashboard.html', context)
