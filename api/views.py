from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action

from api.serializers import UserSerializer
from .models import Movie, Review, Actor
from .serializers import MovieSerializer, ReviewSerializer, ActorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        #movies = Movie.objects.filter(after_premiere=True)
        movies = Movie.objects.all()
        return movies

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        #if request.user.is_superuser:
        movie = Movie.objects.create(tittle=request.data['tittle'],
                               describe=request.data['describe'],
                               after_premiere=request.data['after_premiere'],
                               premiere=request.data['premiere'],
                               year=request.data['year'],
                               imdb_rating=['imdb_rating'])
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)
        #else:
        #    return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.tittle = request.data['tittle']
        movie.describe = request.data['describe']
        movie.after_premiere = request.data['after_premiere']
        movie.premiere=request.data['premiere']
        movie.year=request.data['year']
        movie.imdb_rating=['imdb_rating']

        movie.save()

        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.delete()
        return Response('Movie deleted')

    @action(detail=True)
    def premiere(self, request, **kwargs):
        movie = self.get_object()
        movie.after_premiere = True
        movie.save()

        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def premiere_all(self, request, **kwargs):
        movies = Movie.objects.all()
        movies.update(after_premiere=request.data['after_premiere'])

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer