from django.db import models
from django.contrib.auth.models import User
from movieseries.models import Movie
# Create your models here.


class MyList(models.Model):

    id = models.AutoField(
        primary_key=True,
        default=1
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    show = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
    )
    # series

    def __str__(self):
        return str(self.user_id)
