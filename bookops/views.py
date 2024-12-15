from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import User
from manuscript.models import Manuscript

# Home page render
def index_view(request):
    return render(request, "bookops/index.html")

# Registration page render
def register_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm = request.POST["confirmation"]
        if password != confirm:
            return render(request, "bookops/register.html", {
                "message": "Passwords do not match.",
            })
        editor = request.POST.get("editor", False)
        if editor == "on":
            editor = True

        try:
            user = User.objects.create_user(name, email, password, editor=editor)
            user.save()
        except IntegrityError:
            print(IntegrityError)
            return render(request, "bookops/register.html", {
                "message": "Username or email address already taken.",
            })
        
        login(request, user)

        return HttpResponseRedirect(reverse("index"))
    
    # GET
    else:
        return render(request, "bookops/register.html")

# Login render
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        username = User.objects.get(email=email).username
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "bookops/login.html", {
                "message": "Login invalid."
            })
    else:
        return render(request, "bookops/login.html")

# Account page render
def account_view(request):
    
    user = request.user
    
    manuscripts = Manuscript.objects.filter(author=user)
    editing = Manuscript.objects.filter(editor=user)
    
    return render(request, "bookops/account.html", {
        "manuscripts" : manuscripts,
        "editing": editing,
    })

# Logout function
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


