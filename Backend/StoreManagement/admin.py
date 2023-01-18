from django.contrib import admin
from StoreManagement.models import Store

# Register your models here.
class StoreAdmin(admin.ModelAdmin):
  list_display= ['storeId', 'storeName', 'sellerProfileIns', 'itemIdList']

admin.site.register(Store, StoreAdmin)
