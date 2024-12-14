from django.shortcuts import render, HttpResponse

# Create your views here.

from manuscript.models import Manuscript
from .models import Buyer, Sale, Lead

import random


def marketing_view(request):
    if request.method == "POST":
        book_id = request.POST["selected-manuscript"]

        book = Manuscript.objects.get(pk=book_id)

        sales_number = random.randint(1, 25)

        for sale in range(sales_number):
            print(sale)
            name = random.choice(["John Doe", "Jane Doe"])
            sex = random.choice(["male", "female"])
            race = random.choice(["white", "black", "asian", "native american", "pacific islander"])
            education = random.choice(["no highschool diploma", "high school", "bachelors", "masters", "doctorate"])
            buyer = Buyer(name=name, age=random.randint(18, 100), sex=sex, race=race, education=education, email="sample@sample.com", address="Anytonwn, USA")
            buyer.save()
            online=random.choice()
            sale= Sale(manuscript=book, buyer=buyer, online=True or False, )

        return render(request, "marketing/marketing.html", {
            "publications": Manuscript.objects.filter(accepted=True)
        })
    else:
        return render(request, "marketing/marketing.html", {
            "publications": Manuscript.objects.filter(accepted=True)
        })  
