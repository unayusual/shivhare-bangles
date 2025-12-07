from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Inquiry
from django.contrib import messages
# Import analytics to log views
from analytics.models import PageVisit, ProductInteraction

def home(request):
    featured_products = Product.objects.all()[:4] # Show top 4
    return render(request, 'store/home.html', {'featured_products': featured_products})

def catalog(request):
    products = Product.objects.all()
    return render(request, 'store/catalog.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    # Simple analytics logging (synchronous for now, ideally async/celery)
    # Log Interaction
    if not request.session.get(f'viewed_{product.id}'):
        try:
            ProductInteraction.objects.create(
                product=product,
                interaction_type='VIEW'
            )
            request.session[f'viewed_{product.id}'] = True
        except Exception:
            pass # Read-only DB

    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        message = request.POST.get('message')
        
        try:
            Inquiry.objects.create(
                product=product,
                customer_name=name,
                contact_number=contact,
                message=message
            )
            
            # Log Enquire Click/Submit
            ProductInteraction.objects.create(
                product=product,
                interaction_type='ENQUIRE_CLICK',
                metadata={'customer': name}
            )
            messages.success(request, 'Your inquiry has been sent successfully! We will contact you shortly.')
        except Exception:
            messages.error(request, 'Inquiry logging is disabled on this Live Demo (Read-only System). Please call us directly.')
            
        return redirect('product_detail', slug=slug)

    return render(request, 'store/product_detail.html', {'product': product})

def about(request):
    return render(request, 'store/about.html')
