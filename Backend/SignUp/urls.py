from django.urls import path
from SignUp.views import SignUp

urlpatterns= [
    path('', SignUp.as_view())
]