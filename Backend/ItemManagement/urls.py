from django.urls import path
from ItemManagement.views import ItemManagement

urlpatterns = [
    path('', ItemManagement.as_view(), name= 'ItemManagement'),
    path('<itemId>', ItemManagement.as_view(), name= 'ItemManagementGet')
]