from django.urls import include
from django.contrib import admin
from django.urls import path
from api import urls
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path('auth/', views.obtain_auth_token)
]
