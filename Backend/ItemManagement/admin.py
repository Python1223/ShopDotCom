from django.contrib import admin
from ItemManagement.models import ItemModel

# Register your models here.
class ItemModelAdmin(admin.ModelAdmin):
    list_display= ['itemId', 'itemName', 'itemPrice']

admin.site.register(ItemModel, ItemModelAdmin)
