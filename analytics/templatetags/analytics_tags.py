from django import template
from django.db.models import Count
from django.utils import timezone
from datetime import timedelta
from analytics.models import PageVisit, ProductInteraction
from store.models import Inquiry

register = template.Library()

@register.inclusion_tag('analytics/partials/dashboard_content.html')
def render_analytics_dashboard():
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)
    
    # 1. Total Visits (Weekly/Monthly)
    visits_week = PageVisit.objects.filter(timestamp__gte=week_ago).count()
    visits_month = PageVisit.objects.filter(timestamp__gte=month_ago).count()
    
    # 2. Interactions
    interactions_week = ProductInteraction.objects.filter(timestamp__gte=week_ago).values('interaction_type').annotate(count=Count('id'))
    
    # 3. Top Products
    top_enquired_products = Inquiry.objects.filter(created_at__gte=month_ago)\
        .values('product__name')\
        .annotate(total=Count('id'))\
        .order_by('-total')[:5]
        
    # 4. Recent Inquiries
    recent_inquiries = Inquiry.objects.select_related('product').order_by('-created_at')[:10]
    
    return {
        'visits_week': visits_week,
        'visits_month': visits_month,
        'interactions_week': interactions_week,
        'top_enquired_products': top_enquired_products,
        'recent_inquiries': recent_inquiries,
    }
