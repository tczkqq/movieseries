from django.shortcuts import render, Http404
from movieseries.models import Movie
# Create your views here.
def index_view(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movieseries/index.html', context)


def detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except:
        raise Http404("Poll does not exist")
    context = {
        'movie':movie
    }
    return render(request, 'movieseries/detail.html', context)
