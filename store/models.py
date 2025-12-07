from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Ideally we use ImageField, but for simplicity/demo without media setup we can use CharField or ImageField.
    # Using ImageField requires creating a media dir and configuring it. I'll stick to ImageField but might need to setup media.
    # Actually, let's use CharField for external URLs if the user wants, but ImageField is better for "listing panel" requirement.
    # I'll use ImageField and setup media settings quickly.
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.CharField(max_length=100, default='General')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Inquiry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='inquiries')
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.product.name if self.product else 'Deleted Product'} by {self.customer_name}"

    class Meta:
        verbose_name_plural = "Inquiries"
