from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'tittle', 'describe', 'after_premiere']

class MovieMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('tittle',)