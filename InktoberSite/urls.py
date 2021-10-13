from django.urls import path
from . import views

# Sets up your urls depending on what you type you go to different views a.k.a pages
urlpatterns = [
    path("", views.home, name = "home"),
    path("FAQ/", views.FAQ, name = "FAQ"),
    path("user/", views.user, name = "user"),
    path("response/", views.inputresponse, name = "inputresponse")
]
