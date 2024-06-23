from django.forms import ModelForm
from .models import Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ["name", "surname"]


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
