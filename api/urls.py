from django.urls import include
from rest_framework import routers
from api import views
from django.urls import path

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet, basename="movie")
router.register(r'reviews', views.ReviewViewSet, basename="review")
router.register(r'actors', views.ActorViewSet, basename="actors")

urlpatterns = [
    path('', include(router.urls)),

]