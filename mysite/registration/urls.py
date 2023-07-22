from django.urls import path
from .views import welcome, RegistrationView, LoginView, SignOutView

urlpatterns = [
    path("", welcome, name="welcome"),
    path("registration", RegistrationView.as_view(), name="registration"),
    path("login", LoginView.as_view(), name="login"),
    path("rooms/logout", SignOutView.as_view(), name="logout")
]

