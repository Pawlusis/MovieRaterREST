from django.contrib.auth.models import User
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action

from api.serializers import UserSerializer
from .models import Movie, Review, Actor
from .serializers import MovieSerializer, ReviewSerializer, ActorSerializer


class MovieySetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('tittle', 'describe', 'year')
    search_fields = ('tittle', 'describe')
    ordering_fields = '__all__'
    ordering = ('year',)
    pagination_class = MovieySetPagination

    def get_queryset(self):
        # year = self.request.query_params.get('year', None)
        # id = self.request.query_params.get('id', None)
        #
        # if id:
        #     movies = Movie.objects.filter(id=id)
        # else:
        #     if year:
        #         movies = Movie.objects.filter(year=year)
        #     else:
        #         movies = Movie.objects.all()
        movies = Movie.objects.all()
        return movies

    # def list(self, request, *args, **kwargs):
    #     tittle = self.request.query_params.get('tittle', None)
    #
    #     #movies = Movie.objects.filter(tittle__exact=tittle)
    #     #movies = Movie.objects.filter(tittle__contains=tittle)
    #     movies = Movie.objects.filter(premiere__describe="2000")
    #
    #     #queryset = self.get_queryset()
    #
    #     serializer = MovieSerializer(movies, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MovieSerializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # if request.user.is_superuser:
        movie = Movie.objects.create(tittle=request.data['tittle'],
                                     describe=request.data['describe'],
                                     after_premiere=request.data['after_premiere'],
                                     year=request.data['year'])
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)
        # else:
        #    return HttpResponseNotAllowed('Not allowed')

    def update(self, request, *args, **kwargs):
        movie = self.get_object()
        movie.tittle = request.data['tittle']
        movie.describe = request.data['describe']
        movie.after_premiere = request.data['after_premiere']
        movie.year = request.data['year']
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
    def all_premiere(self, request, **kwargs):
        movies = Movie.objects.all()
        movies.update(after_premiere=request.data['after_premiere'])

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    @action(detail=True, methods=['post'])
    def merge(self, request, **kwargs):
        actor = self.get_object()
        movie = Movie.objects.get(id=request.data['movie'])
        actor.movies.add(movie)

        serializer = ActorSerializer(actor, many=False)
        return Response(serializer.data)
