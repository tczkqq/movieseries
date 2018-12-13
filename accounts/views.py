from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('core:index')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {'form': form})


@login_required
def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return redirect('core:index')


@login_required
def myprofile_view(request):
    user = User.objects.get(username=request.user)
    context = {
        'user': user
    }
    return render(request, "accounts/myprofile.html", context)


@login_required
def changepass_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            redirect('accounts:myprofile')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/changepass.html', context)
