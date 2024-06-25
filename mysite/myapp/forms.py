from django.forms import ModelForm
from django.forms.widgets import TextInput
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
        fields = ["username","first_name","last_name","email","password1","password2"]
        # widgets = {'first_name': forms.TextInput(attrs={'size': 100})}j
