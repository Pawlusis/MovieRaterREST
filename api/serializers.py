from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, ExtraInfo, Review


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['describe', 'stars', 'movie']
class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['time', 'category']

class MovieSerializer(serializers.ModelSerializer):
    extra_info = ExtraInfoSerializer(many=False)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'tittle', 'describe', 'after_premiere', 'premiere', 'year', 'imdb_rating', 'extra_info', 'reviews')



