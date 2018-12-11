from django.urls import path
from . import views

app_name = 'mylist'

urlpatterns = [
    path('', views.list_view, name="list")
]
