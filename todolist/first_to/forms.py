from django import forms
from .models import Todo

class Userform(forms.ModelForm):
    model=Todo
    fields="__all__"