from django.urls import path
from . import views


app_name = 'movieseries'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('<int:id>/', views.detail_view, name='detail')
] 

