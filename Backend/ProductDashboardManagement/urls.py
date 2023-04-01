from django.urls import path
from ProductDashboardManagement.views import ProductDashboardManagement

urlpatterns= [
    path('', ProductDashboardManagement.as_view(), name= 'ProductDashboard')
]