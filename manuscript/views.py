import json
from django.shortcuts import HttpResponse, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Manuscript

# Rendering of base page
def manuscripts(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "manuscript/editor.html")

# Endpoint for getting manuscript set
def get_manuscripts(request, get):
    if get == "accepted":
        manuscripts = Manuscript.objects.filter(accepted=True)
    elif get == "my":
        manuscripts = Manuscript.objects.filter(
            accepted=True,
            editor=request.user
        )

    manuscripts = manuscripts.order_by("-timestamp").all()
    return JsonResponse([manuscript.serialize() for manuscript in manuscripts], safe=False)

# Endpoint for getting specific manuscript
@csrf_exempt
def get_manuscript(request, id):
    manuscript = Manuscript.objects.get(pk=id)
    
    if request.method == "PUT":
        manuscript.accepted = True
        manuscript.save()
        return HttpResponse(status=204)
    else:    
        return JsonResponse(manuscript.serialize())

# Endpoint for the save button on the editing page
@csrf_exempt
def edit_manuscript(request, id):
    manuscript = Manuscript.objects.get(pk=id)

    if request.method == "PUT":
        data = json.loads(request.body)
        manuscript.title = data.get("title")
        manuscript.synopsis = data.get("synopsis")
        manuscript.body = data.get("body")
        manuscript.save()
        return HttpResponse(status=204)