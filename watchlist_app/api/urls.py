from django.urls import path
from watchlist_app.api.views import MovieListView, MovieDetailView



urlpatterns = [
     path('list/', MovieListView.as_view(), name='movie-list'),
     path('<int:pk>/', MovieDetailView.as_view(), name='movie-details'),
]

# from watchlist_app.api.views import movie_list, movie_details

# urlpatterns = [
#      path('list/', movie_list, name='movie-list'),
#      path('<int:pk>/', movie_details, name='movie-details'),
# ]
