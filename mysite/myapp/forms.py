from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Users, Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ["name", "surname"]


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
        # widgets = {'first_name': forms.TextInput(attrs={'size': 100})}


class UserUpdateForm(UserChangeForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        error_messages={"required": "You must enter your current password."},
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

    def clean(self):
        cleaned_data = super().clean()
        current_password = self.cleaned_data.get("password1")

        if not current_password:
            return cleaned_data
        else:
            if not self.instance.check_password(current_password):
                self.add_error("password1", "Incorrect current password.")

        return cleaned_data


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("image",)
