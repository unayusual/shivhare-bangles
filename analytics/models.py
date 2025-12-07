from django.db import models

class PageVisit(models.Model):
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True, null=True)
    # We can try to session tracking
    session_id = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Visit to {self.path} at {self.timestamp}"

class ProductInteraction(models.Model):
    # Could be 'VIEW', 'CLICK_ENQUIRE', 'TIME_SPENT'
    INTERACTION_TYPES = [
        ('VIEW', 'View Product'),
        ('ENQUIRE_CLICK', 'Clicked Enquire'),
    ]
    
    # product_id field is automatically handled by the ForeignKey 'product'
    # To avoid circular imports, maybe just store ID or use string reference.
    # Let's use string reference 'store.Product'
    product = models.ForeignKey('store.Product', on_delete=models.CASCADE, related_name='interactions')
    
    interaction_type = models.CharField(max_length=50, choices=INTERACTION_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict, blank=True) # For "time spent" etc

    def __str__(self):
        return f"{self.interaction_type} on {self.product_id}"
