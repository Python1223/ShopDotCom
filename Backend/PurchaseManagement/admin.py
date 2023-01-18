from django.contrib import admin
from PurchaseManagement.models import PurchaseListModel

class PurchaseListModelAdmin(admin.ModelAdmin):
  list_display= ['purchaseListId', 'buyerProfileIns', 'purchaseIdList']

admin.site.register(PurchaseListModel, PurchaseListModelAdmin)
