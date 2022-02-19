from django import forms
from .models import Owner_Data, Pet_Data


class Owners_Form(forms.ModelForm):
    class Meta:
        model = Owner_Data
        fields = ["owner_name_surname", "owner_age", "owner_mail", "owner_phone", "owner_adress"]    
        
class Pets_Form(forms.ModelForm):
    class Meta: 
        model = Pet_Data
        the_owner_of_pet = Owners_Form
        fields = ["the_owner_of_pet","pet_familia","pet_species","pet_name","pet_age","pet_description"]
        

