from django.shortcuts import render, HttpResponse

# Create your views here.

def marketing_view(request):
    return render(request, "marketing/marketing.html")