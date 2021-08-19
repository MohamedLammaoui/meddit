from django.urls import path
from .views import home, login, signup

urlpatterns = [
    path('', home, name="home"),
    path("signup", signup, name="signup")
]