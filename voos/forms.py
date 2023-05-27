from .models import *
from django.forms import ModelForm
from django import forms

class PassageiroForm(ModelForm):
    class Meta:
        model = Passageiro
        fields = ['nome']


class VooForm(ModelForm):
    class Meta:
        model = Passageiro
        fields = ['voos']
        labels = {'voos':''}
        help_texts = {'voos': 'Premir Ctrl para selecionar mais do que um'}
