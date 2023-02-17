from django.contrib import admin
from ItemManagement.models import ItemModel

# Register your models here.
class ItemModelAdmin(admin.ModelAdmin):
    list_display= [ 'itemId', 'itemName' ,'itemDetails' ,'itemPrice', 'sellerProfile', 
                    'itemCategory', 'itemImage']

admin.site.register(ItemModel, ItemModelAdmin)
