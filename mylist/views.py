from django.shortcuts import render
from .models import MyList

# Create your views here.


def list_view(request):
    mylist = MyList.objects.filter(user_id=request.user)
    context = {
        'list': mylist
    }
    return render(request, 'mylist/list.html', context)
