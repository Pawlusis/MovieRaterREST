from django.urls import include
from rest_framework import routers
from api import views
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),

]