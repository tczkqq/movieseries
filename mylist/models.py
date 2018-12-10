from django.db import models
from django.contrib.auth.models import User
from movieseries.models import Movie
# Create your models here.


class MyList(models.Model):

    id = models.AutoField(
        primary_key=True
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    movies = models.ManyToManyField(
        Movie,
        blank=True
    )
    # series
