from django import forms
from .models import Post


class UserRegister(forms.ModelForm):
    