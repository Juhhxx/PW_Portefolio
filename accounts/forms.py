from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, label='Name', required=True)
    last_name = forms.CharField(max_length=100, label='Last_Name', required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]