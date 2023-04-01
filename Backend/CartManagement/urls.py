from django.urls import path
from CartManagement.views import CartManagement, ItemInCart

urlpatterns= [
    path('<operation>', CartManagement.as_view(), name= 'Cart Management'),
    path('ItemInCart/<itemId>', ItemInCart.as_view(), name= 'Item in Cart'),
]
