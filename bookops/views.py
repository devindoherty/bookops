from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import User

def index_view(request):
    # return HttpResponse("<a href='/slush'>BOOK OPS</a>")
    return render(request, "bookops/index.html")

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

def account_view(request):
    return render(request, "bookops/account.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


