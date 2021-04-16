from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import status, views

from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


class MovieListView(views.APIView):
  def get(self, request, format=None):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, *args, format=None, **kwargs):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class MovieDetailView(views.APIView):
  def get(self, request, *args, format=None, **kwargs):
    try:
      movie = Movie.objects.get(pk=kwargs.get('pk'))
    except Movie.DoesNotExist:
      return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)

  
  def put(self, request, *args, format=None, **kwargs):
    try:
      movie = Movie.objects.get(pk=kwargs.get('pk'))
    except Movie.DoesNotExist:
      return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, *args, format=None, **kwargs):
    try:
      movie = Movie.objects.get(pk=kwargs.get('pk'))
    except Movie.DoesNotExist:
      return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)





















# @api_view(['GET', 'POST'])
# def movie_list(request):
#   if request.method == "GET":
#     movies = Movie.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)
  
#   if request.method == 'POST':
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)

# @api_view(['GET','PUT', 'DELETE', 'PATCH'])
# def movie_details(request, pk):
#   if request.method == 'GET':
#     try:
#       movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#       return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
#     serializer = MovieSerializer(movie)  
#     return Response(serializer.data, status=status.HTTP_200_OK)

#   if request.method == 'PUT':
#     movie = Movie.objects.get(pk=pk)
#     serializer = MovieSerializer(movie, data=request.data)
#     if serializer.is_valid(raise_exception=True):
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)

#   if request.method == 'DELETE':
#     movie = Movie.objects.get(pk=pk)
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)    