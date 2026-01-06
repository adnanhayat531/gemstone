from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('collection/', views.gemstone_list, name='gemstone_list'),
    path('gemstone/<slug:slug>/', views.gemstone_detail, name='gemstone_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/toggle/<int:gemstone_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('journal/', views.blog_list, name='blog_list'),
    path('journal/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('inquire/<int:gemstone_id>/', views.inquire_gemstone, name='inquire_gemstone'),
]
