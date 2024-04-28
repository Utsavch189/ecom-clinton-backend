from django.contrib import admin
from .models import *

admin.site.register(UserRole)
admin.site.register(User)
admin.site.register(UserAddress)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
admin.site.register(VariantOptions)
admin.site.register(ProductInventory)
admin.site.register(ProductDiscount)
admin.site.register(Product)
admin.site.register(ProductVarient)
admin.site.register(VarientAttribute)
admin.site.register(ProductAttachment)
admin.site.register(CartItem)
admin.site.register(ProductOrderToDeliveryStatus)
admin.site.register(Payment)
admin.site.register(Invoice)
admin.site.register(Order)
admin.site.register(ErrorLog)
admin.site.register(AccessLog)

