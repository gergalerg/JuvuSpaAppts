from django.contrib.auth.models import User
from django import forms


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            )
