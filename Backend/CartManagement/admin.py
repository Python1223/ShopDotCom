from django.contrib import admin
from CartManagement.models import CartModel

class CartModelAdmin(admin.ModelAdmin):
    list_display= ['cartId', 'buyerProfileIns', 'itemIdList']

admin.site.register(CartModel, CartModelAdmin)
