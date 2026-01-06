from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Gemstone, ContactMessage, Subscriber

from django.db.models import Q
from .models import Gemstone, ContactMessage, Subscriber, Testimonial, BlogPost

def home(request):
    featured_gemstones = Gemstone.objects.filter(featured=True)[:6]
    testimonials = Testimonial.objects.all().order_by('-created_at')[:3]
    return render(request, 'store/home.html', {
        'featured_gemstones': featured_gemstones,
        'testimonials': testimonials
    })

def gemstone_list(request):
    gemstones = Gemstone.objects.all()
    
    # Search
    query = request.GET.get('q')
    if query:
        gemstones = gemstones.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(category__icontains=query))

    # Filtering
    category = request.GET.get('category')
    if category:
        gemstones = gemstones.filter(category=category)
    
    origin = request.GET.get('origin')
    if origin:
        gemstones = gemstones.filter(origin__icontains=origin)
        
    # Sorting
    sort_by = request.GET.get('sort')
    if sort_by == 'price_asc':
        gemstones = gemstones.order_by('price')
    elif sort_by == 'price_desc':
        gemstones = gemstones.order_by('-price')
    elif sort_by == 'newest':
        gemstones = gemstones.order_by('-created_at')

    return render(request, 'store/gemstone_list.html', {'gemstones': gemstones})

def gemstone_detail(request, slug):
    gemstone = get_object_or_404(Gemstone, slug=slug)
    related_gemstones = Gemstone.objects.filter(category=gemstone.category).exclude(id=gemstone.id)[:3]
    return render(request, 'store/gemstone_detail.html', {'gemstone': gemstone, 'related_gemstones': related_gemstones})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=message)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
        
    return render(request, 'store/contact.html')

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.warning(request, 'You are already subscribed.')
    return redirect('home')

def toggle_wishlist(request, gemstone_id):
    # Get current wishlist from session, or empty list
    wishlist = request.session.get('wishlist', [])
    
    if gemstone_id in wishlist:
        wishlist.remove(gemstone_id)
        messages.info(request, 'Removed from wishlist.')
    else:
        wishlist.append(gemstone_id)
        messages.success(request, 'Added to wishlist!')
    
    # Save back to session
    request.session['wishlist'] = wishlist
    
    # Redirect to where the user came from
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def wishlist(request):
    wishlist_ids = request.session.get('wishlist', [])
    gemstones = Gemstone.objects.filter(id__in=wishlist_ids)
    return render(request, 'store/wishlist.html', {'gemstones': gemstones})

def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, 'store/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'store/blog_detail.html', {'post': post})

def inquire_gemstone(request, gemstone_id):
    if request.method == 'POST':
        gemstone = get_object_or_404(Gemstone, id=gemstone_id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Prepend gemstone info to message to ensure context
        full_message = f"Inquiry about {gemstone.name} (Ref: {gemstone.slug}):\n{message}"
        
        ContactMessage.objects.create(name=name, email=email, phone=phone, message=full_message)
        messages.success(request, f'Thank you! We have received your inquiry about the {gemstone.name}.')
        return redirect('gemstone_detail', slug=gemstone.slug)
    return redirect('gemstone_list')
