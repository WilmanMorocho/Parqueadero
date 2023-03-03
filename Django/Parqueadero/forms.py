from dataclasses import fields
from django import forms
from .models import *


class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'


class propietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'


class parqueoForm(forms.ModelForm):
    class Meta:
        model = Parqueo
        fields = '__all__'
