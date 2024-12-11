from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def slush_view(request):
    if request.method == "POST":
        print(request.POST)
        
    else:
        return render(request, "slush/slush.html")