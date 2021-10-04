from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

# Creating view a.k.a 
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    return render(response, "InktoberSite/base.html", {})

def home(response):
    # TODO: Make it 
    return render(response, "InktoberSite/home.html", {})
