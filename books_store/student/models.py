from django.db import models
from django import forms
from home.models import *
# Create your models here.

class bookform(forms.ModelForm):
    class Meta:
        model = book
        fields = ['name']