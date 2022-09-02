from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    code = forms.CharField(required=True, max_length=32, min_length=32)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'code']

