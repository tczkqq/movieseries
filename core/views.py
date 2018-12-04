from django.shortcuts import render
from movieseries.models import Movie

# Create your views here.


def index_view(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, "core/index.html", context)
