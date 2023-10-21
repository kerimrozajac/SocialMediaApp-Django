from django.contrib import admin
from django.urls import path, include
from . import views
from accounts.custom_views import CustomRegisterView, CustomLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("api/v1/", include("posts.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path('api/v1/dj-rest-auth/login/', CustomLoginView.as_view(), name='custom_login'),
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")),  # new
    path('api/v1/dj-rest-auth/registration/', CustomRegisterView.as_view(), name='custom_register'),
    path('csrf_token/', views.get_csrf_token, name='get_csrf_token'),
]
