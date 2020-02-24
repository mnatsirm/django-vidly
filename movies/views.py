from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie


def index(request):
    # get list of movies
    movies = Movie.objects.all()
    output = ', '.join([m.title for m in movies])

    # filter list
    # Movie.objects.filter(release_year=1984)

    # # get specific movie
    # Movie.objects.get(id=1)
    return HttpResponse(output)
