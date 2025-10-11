from django.urls import path
from . import views

urlpatterns = [
    path("", views.movie_list, name="movie_list"),
    path("movies/new/", views.movie_create, name="movie_create"),
    path("movies/<int:pk>/", views.movie_detail, name="movie_detail"),
    path("movies/<int:pk>/edit/", views.movie_update, name="movie_update"),
    path("movies/<int:pk>/delete/", views.movie_delete, name="movie_delete"),
]
