from django.urls import path
from . import views

# Sets up your urls depending on what you type you go to different views a.k.a pages
urlpatterns = [
    path("<str:name>", views.index, name="index"),
    path("", views.home, name = "home")
]