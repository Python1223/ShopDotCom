from django.contrib import admin
from ProfileManagement.models import BuyerProfileModel, SellerProfileModel

# Register your models here.

class BuyerProfileModelAdmin(admin.ModelAdmin):
    list_display= ['userModelIns','cartId','purchaseListId','orderListId','profileType']

class SellerProfileModelAdmin(admin.ModelAdmin):
    list_display= ['userModelIns','storeId','storeName','profileType']


admin.site.register(BuyerProfileModel, BuyerProfileModelAdmin)
admin.site.register(SellerProfileModel, SellerProfileModelAdmin)