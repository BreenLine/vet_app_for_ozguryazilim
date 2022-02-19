from django.shortcuts import render
from django.http import HttpResponse
from .models import Owner_Data, Pet_Data
from .forms import Owners_Form, Pets_Form

# Create your views here.


def index(request):
    the_owners = Owner_Data.objects.all()
    the_pets = Pet_Data.objects.all()
    return render(request, "pages/index.html", {"show_owner_data":the_owners,"show_pet_data":the_pets})

def test(request):
    return render(request, "pages/test.html")

def create(request):
    the_owners = Owner_Data.objects.all()
    the_pets = Pet_Data.objects.all()
    if request.method == "POST":
        form = Owners_Form(request.POST or None)
        form_2 = Pets_Form(request.POST or None)
        if form.is_valid() and form_2.is_valid():
            form.save()
            form_2.save()
            return render(request, "pages/create.html", {"show_owner_data":the_owners,"show_pet_data":the_pets},)
    else:

        return render(request, "pages/create.html", {"show_owner_data":the_owners,"show_pet_data":the_pets})