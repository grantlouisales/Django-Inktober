from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import UserInfo
from .models import User, Video

# Create your views here.

# Creating view a.k.a page
def home(response):
    """
    This is the home page for the Inktober website.

    Purpose: Purpose of this webpage is to show the most important information
    in the website. This will be the page the that will show the 
    overview of the website.
    """
    videos = Video.objects.all()
    context = {
        "videos" : videos
    }

    return render(response, "InktoberSite/home.html", context)

def FAQ(response):
    """
    This is the information page for the Inktober website.

    Purpose: The purpose of this webpage is to show all of the extra information
    about Inktober. This will include anything such as types of pens to types of
    sketchbooks or prompts. This will also show a random years inktober prompts
    given.
    """
    return render(response, "InktoberSite/FAQ.html", {})


def user(response):
    """
    This is the user page for the Inktober website.

    Purpose: The purpose of this page is to grab information from the
    user like first name, last name, email, and text submission box. This
    text submission box is going to be used for a response from the user. The 
    text box will ask for a inktober prompt. It will then try to store the user's
    information in a database of some sort when I have time to.
    """

    # Saying that if the response is post make the users form submission hidden
    # else leave it unhidden.
    if response.method == "POST":
        form = UserInfo(response.POST)

        if form.is_valid():
            n = form.cleaned_data["fname"]
            t = User(fname = n)
            t.save()
            return HttpResponseRedirect("/response")
    else:
        form = UserInfo()

    return render(response, "InktoberSite/user.html", {"form":form})

def inputresponse(response):
    return render(response, "InktoberSite/userInputResponse.html", {})
