from django.urls import path
from LogIn.views import LogIn

urlpatterns= [
    path('', LogIn.as_view())
]