from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def slush(request):
    return HttpResponse("<a href='/'>SLUSH</a>")