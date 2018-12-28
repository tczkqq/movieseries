from django.forms import ModelForm
from . import models


class CreateComment(ModelForm):

    class Meta:

        model = models.Comment
        fields = ['text']
