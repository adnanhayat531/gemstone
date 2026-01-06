from django.contrib import admin
from django.utils.html import format_html
from .models import Gemstone, ContactMessage, Subscriber, Testimonial, BlogPost

@admin.register(Gemstone)
class GemstoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'carat', 'featured', 'image_preview')
    list_filter = ('category', 'featured', 'origin')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('featured', 'price')
    readonly_fields = ('image_preview_large',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return ""
    image_preview.short_description = 'Image'

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-width: 300px; height: auto;" />', obj.image.url)
        return ""
    image_preview_large.short_description = 'Image Preview'

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    ordering = ('-created_at',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('name', 'text')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_filter = ('is_published',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'message', 'created_at')
    
    def has_add_permission(self, request):
        return False
