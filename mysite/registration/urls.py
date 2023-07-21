from django.urls import path
from .views import welcome, RegistrationView, LoginView, home_page

urlpatterns = [
    path("", welcome, name="welcome"),
    path("registration", RegistrationView.as_view(), name="registration"),
    path("login", LoginView.as_view(), name="login"),
    path("home_page", home_page, name="home_page"),
]

