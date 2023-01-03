from django.contrib import admin
from OrderManagement.models import OrderModel

class OrderModelAdmin(admin.ModelAdmin):
    list_display= ['orderId', 'buyerProfileModelIns', 'itemIns', 'paymentStatus', 'deliveryStatus']


admin.site.register(OrderModel, OrderModelAdmin)
