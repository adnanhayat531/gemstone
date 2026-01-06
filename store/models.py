from django.db import models
from django.utils.text import slugify

class Gemstone(models.Model):
    CATEGORY_CHOICES = (
        ('Ruby', 'Ruby'),
        ('Sapphire', 'Sapphire'),
        ('Emerald', 'Emerald'),
        ('Diamond', 'Diamond'),
        ('Amethyst', 'Amethyst'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    origin = models.CharField(max_length=100)
    carat = models.DecimalField(max_digits=5, decimal_places=2)
    treatment = models.CharField(max_length=100, blank=True, help_text="e.g. Heat, None")
    certification = models.CharField(max_length=100, blank=True, help_text="e.g. GIA, GRS")
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='gemstones/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, help_text="e.g. Collector, Jewelry Designer")
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, help_text="1 to 5 stars")
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating} stars)"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
