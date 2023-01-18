from django.contrib import admin
from OrderManagement.models import OrderModel, OrderListModel

class OrderModelAdmin(admin.ModelAdmin):
    list_display= ['orderId', 'buyerProfileIns', 'itemIns']

class OrderListModelAdmin(admin.ModelAdmin):
    list_display= ['orderListId', 'buyerProfileIns', 'orderIdList']

admin.site.register(OrderModel, OrderModelAdmin)
admin.site.register(OrderListModel, OrderListModelAdmin)
                       