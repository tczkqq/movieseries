from django.urls import path, include
from . import views

app_name = "accounts"

urlpatterns = [
    path('password', views.changepass_view, name="changepass"),
    path('myprofile', views.myprofile_view, name="myprofile"),
    path('login', views.login_view, name="login"),
    path('register', views.register_view, name="register"),
    path('logout', views.logout_view, name="logout"),
]
