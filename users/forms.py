from  django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ("email","first_name","last_name")

class CustomUserChangeForm(UserChangeForm ):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = CustomUser
        fields = ("email","first_name","last_name")