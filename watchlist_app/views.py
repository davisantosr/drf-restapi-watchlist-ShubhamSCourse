from django.shortcuts import render
from django.http import JsonResponse

from watchlist_app.models import *

def movie_list(request):
  movies = Movie.objects.all()
  movies = list(movies.values())
  data = {
    'movies': movies
    }

  return JsonResponse(data)