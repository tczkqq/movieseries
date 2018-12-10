from django.shortcuts import render

# Create your views here.


def list_view(request):
    context = {

    }
    return render(request, 'mylist/list.html', context)
