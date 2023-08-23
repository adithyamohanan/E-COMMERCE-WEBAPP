from django.contrib import admin
from .models import *
# Register your models here.

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_product_name', 'address_line1',  'address_line2', 'city', 'state', 'postal_code', 'country')
    
    def get_product_name(self, obj):
        return obj.product.name if obj.product else ''
    
    get_product_name.short_description = 'Product Name'
admin.site.register(Product)
admin.site.register(order)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Order_Successful)