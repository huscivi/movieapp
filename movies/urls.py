from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),   # http://127.0.0.1:8000/
    path("home", views.home),   # http://127.0.0.1:8000/home
    path("movies", views.movies)   # http://127.0.0.1:8000/movies
]