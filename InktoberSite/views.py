from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import User

# Create your views here.

# Creating view a.k.a page
def home(response):
    """
    This is the home page for the Inktober website.

    Purpose: Purpose of this webpage is to show the most important information
    in the website. This will be the page the that will show the 
    overview of the website.
    """
    return render(response, "InktoberSite/home.html", {})

def info(response):
    return render(response, "InktoberSite/info.html", {})


def user(response):
    form = User()
    return render(response, "InktoberSite/user.html", {"form":form})