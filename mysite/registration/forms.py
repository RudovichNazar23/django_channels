from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(
        label="Your email",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-control"}),
        min_length=8,
    )
    password2 = forms.CharField(
        required=True,
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          "class": "form-control"})
    )

    def clean_username(self):
        new_user = self.cleaned_data.get("username")
        if User.objects.filter(username=new_user):
            raise ValidationError(
                "This user already exists"
            )
        return new_user

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                "The two password fields didn’t match."
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data.get("username"),
            password=self.cleaned_data.get("password1")
        )
        return user


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Field",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={"class": "form-control"}
                                   )
    )





