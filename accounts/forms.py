from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "display_name", "bio")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "display_name", "bio")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }
