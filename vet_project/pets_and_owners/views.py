from sre_parse import Verbose
from tabnanny import verbose
from django.shortcuts import redirect, render
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
    print(request.pet_familia)
    if request.method == "POST":
        form = Owners_Form(request.POST or None)
        if form.is_valid():
            form.save()
            
            return render(request, "pages/create.html", {"show_owner_data":the_owners,"show_pet_data":the_pets},)
            
    else:
        print(request)
        return render(request, "pages/create.html", {"show_owner_data":the_owners,"show_pet_data":the_pets})

def delete(requets, Owner_Data_id):
    o_data_del = Owner_Data.objects.get(pk=Owner_Data_id)
    o_data_del.delete()
    return redirect("index")        


def update(request, Owner_Data_id):

    if request.method == "POST":
        o_data_up = Owner_Data.objects.get(pk=Owner_Data_id)
        form = Owners_Form(request.POST or None, instance=o_data_up)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        
        return render(request, "pages/update.html")

    return