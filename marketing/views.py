from django.shortcuts import render, HttpResponse

# Create your views here.

from manuscript.models import Manuscript
from .models import Buyer, Sale, Lead

import random

# On POST generates a set of fake sales and buyer data
# On Get displays the marketing page
def marketing_view(request):
    if request.method == "POST":
        book_id = request.POST["selected-manuscript"]

        book = Manuscript.objects.get(pk=book_id)
        Sale.objects.filter(manuscript=book).delete()
        Buyer.objects.all().delete()

        sales_number = random.randint(1, 25)


        for i in range(sales_number):
            name = random.choice(["John Doe", "Jane Doe"])
            sex = random.choice(["male", "female"])
            race = random.choice(["white", "black", "asian", "native american", "pacific islander"])
            education = random.choice(["no highschool diploma", "high school", "bachelors", "masters", "doctorate"])
            buyer = Buyer(name=name, age=random.randint(18, 100), sex=sex, race=race, education=education, email="sample@sample.com", address="Anytonwn, USA")
            buyer.save()
            
            online=bool(random.getrandbits(1))
            location = random.choice(["Chicago", "New York", "Los Angeles", "Seattle", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "Jacksonville", "Austin", "Fort Worth", "Washington, DC", "Columbus", "Indianapolis"])
            sale= Sale(manuscript=book, buyer=buyer, online=online, location=location)
            sale.save()

        return render(request, "marketing/marketing.html", {
            "publications": Manuscript.objects.filter(accepted=True),
            "sales": Sale.objects.filter(manuscript=book)
        })
    else:
        return render(request, "marketing/marketing.html", {
            "publications": Manuscript.objects.filter(accepted=True)
        })  
