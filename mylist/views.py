from django.shortcuts import render
from .models import MyList
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def list_view(request):
    mylist = MyList.objects.filter(user_id=request.user)
    context = {
        'list': mylist
    }
    return render(request, 'mylist/mylist.html', context)
