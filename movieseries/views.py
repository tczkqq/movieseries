from django.shortcuts import render, Http404, redirect
from movieseries.models import Movie
from . import forms
# Create your views here.


def index_view(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movieseries/index.html', context)


def detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)

    except:
        raise Http404("Poll does not exist")

    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            instance.movie_set.add(movie)
            return redirect('movieseries:detail', id=id)
    else:
        form = forms.CreateComment()

    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movieseries/detail.html', context)
