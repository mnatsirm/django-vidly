from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    # get list of movies
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

    # filter list
    # Movie.objects.filter(release_year=1984)

    # # get specific movie
    # Movie.objects.get(id=1)
