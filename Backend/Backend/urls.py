from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from LogIn import urls as LogInUrls
from SignUp import urls as SignUpUrls
from ItemManagement import urls as ItemManagementUrls
from Backend import settings
from ProfileManagement import views as VVVVIEWS

urlpatterns = [
    path('admin', admin.site.urls),

     #JWT urls
    path('getToken',TokenObtainPairView.as_view(),name= 'getToken'),
    path('refreshToken',TokenRefreshView.as_view(),name= 'refreshToken'),
    path('verifyToken',TokenVerifyView.as_view(),name= 'verifyToken'),

    path('Login', include(LogInUrls)),
    path('Signup', include(SignUpUrls)),

    path('Item/', include(ItemManagementUrls)),
    path('Profile/', VVVVIEWS.Profile.as_view(),name= "dadda")
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)