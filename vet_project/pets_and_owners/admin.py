from django.contrib import admin
from .models import Owner_Data, Pet_Data
# Register your models here.


admin.site.register(Owner_Data)
admin.site.register(Pet_Data)