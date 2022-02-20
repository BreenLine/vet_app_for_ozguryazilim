
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.test, name="test"),
    path('create/', views.create, name="create"),
    path('delete/<Owner_Data_id>', views.delete, name="delete"),
    path('update/<Owner_Data_id>', views.update, name="update"),
    
]