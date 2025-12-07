from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Inquiry

class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'name', 'price', 'category', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

class InquiryAdmin(admin.ModelAdmin):
    list_display = ('product_image', 'product', 'customer_name', 'contact_number', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('customer_name', 'contact_number')
    readonly_fields = ('created_at', 'product', 'customer_name', 'contact_number', 'message')

    def product_image(self, obj):
        if obj.product and obj.product.image:
            return format_html('<img src="{}" style="width: 40px; height: 40px; object-fit: cover; border-radius: 4px;" />', obj.product.image.url)
        return "-"
    product_image.short_description = 'Item'

    def has_add_permission(self, request):
        return False # Inquiries are created by users, not admins

admin.site.register(Product, ProductAdmin)
admin.site.register(Inquiry, InquiryAdmin)
