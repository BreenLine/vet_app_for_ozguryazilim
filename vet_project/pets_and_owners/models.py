from django.db import models

# Create your models here.

class Owner_Data(models.Model):
    owner_name_surname = models.CharField(max_length=150)
    owner_age = models.IntegerField()
    owner_mail = models.EmailField(max_length=200)
    owner_phone = models.IntegerField()
    owner_adress = models.TextField(max_length=500)

    def __str__(self):
        return self.owner_name_surname
    

class Pet_Data(models.Model):
    the_owner_of_pet = models.ForeignKey(Owner_Data, on_delete=models.CASCADE)
    pet_familia = models.CharField(max_length=100)
    pet_species = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=150)
    pet_age = models.IntegerField()
    pet_description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.pet_name
    
