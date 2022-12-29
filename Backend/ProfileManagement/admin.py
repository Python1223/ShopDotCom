from django.contrib import admin
from ProfileManagement.models import ProfileModel, BuyerProfileModel, SellerProfileModel

# Register your models here.
class ProfileModelAdmin(admin.ModelAdmin):
    list_display= ['profileId','userIns','profileType']

class BuyerProfileModelAdmin(admin.ModelAdmin):
    list_display= ['profileModelIns','cartId','purchaseListId','orderListId']

class SellerProfileModelAdmin(admin.ModelAdmin):
    list_display= ['profileModelIns','storeName']

admin.site.register(ProfileModel, ProfileModelAdmin)
admin.site.register(BuyerProfileModel, BuyerProfileModelAdmin)
admin.site.register(SellerProfileModel, SellerProfileModelAdmin)