from attr import fields
from django import forms
from django.forms import ModelForm
from .models import *


class ApartmanForm(ModelForm):
    class Meta:
        model = Apartman
        fields = '__all__'

class RecenzijaForm(ModelForm):
    class Meta:
        model = Recenzija
        fields = '__all__'