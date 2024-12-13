from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from manuscript.models import Manuscript

def slush_view(request):
    if request.method == "POST":
        author = request.user
        title = request.POST["title"]
        synopsis = request.POST["synopsis"]
        body = request.POST["body"]

        manuscript = Manuscript(
            author=author, 
            title=title, 
            synopsis=synopsis, 
            body=body,
            editor=author
        )
        manuscript.save()

        return render(request, "slush/slush.html", {
            "submissions": Manuscript.objects.all()
        })
    
    else:
        return render(request, "slush/slush.html", {
            "submissions": Manuscript.objects.all()
        })
    
def read_view(request, id):
    print(id)
    if request.method == "POST":
        pass
    else:
        return render(request, "slush/read.html", {
            "manuscript": Manuscript.objects.get(pk=id)
        })