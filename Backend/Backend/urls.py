from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from LogIn import urls as LogInUrls
from SignUp import urls as SignUpUrls
from ItemManagement import urls as ItemManagementUrls
from ProductDashboardManagement import urls as ProductDashboardUrls
from CartManagement import urls as CartManagementUrls
from ProfileManagement import views as VVVVIEWS
from reverse_image_search.views import ReverseImageSearch
from Backend import settings

urlpatterns = [
    path('admin', admin.site.urls),

     #JWT urls
    path('getToken',TokenObtainPairView.as_view(),name= 'getToken'),
    path('refreshToken',TokenRefreshView.as_view(),name= 'refreshToken'),
    path('verifyToken',TokenVerifyView.as_view(),name= 'verifyToken'),

    path('Login', include(LogInUrls)),
    path('Signup', include(SignUpUrls)),

    path('Item/', include(ItemManagementUrls)),
    path('Profile/', VVVVIEWS.Profile.as_view(),name= "dadda"),

    # Cart Url
    path('Cart/', include(CartManagementUrls)),

    # Product Dashboard Url
    path('ProductDashboard/', include(ProductDashboardUrls)),

    path('aaa/', ReverseImageSearch.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)