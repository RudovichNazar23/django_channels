from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate


def welcome(request):
    return render(request, "registration/welcome.html")


def home_page(request):
    return render(request, "registration/home_page.html", {})


class RegistrationView(View):
    template_name = "registration/registration.html"

    def get(self, request):
        context = {
            "form": RegistrationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("/home_page")
        else:
            return render(request, self.template_name, context)


class LoginView(View):
    template_name = "registration/login.html"
    success_url = "home_page"

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(self.success_url)
            else:
                messages.error(request, "You have wrong email or password, please try again...")
                return render(request, self.template_name, {"form": form})

