from email.policy import default
from django.db import models
from django.core.files.storage import FileSystemStorage
from Simple_Store_D.config import settings_core
from Simple_Store_D.settings import MEDIA_ROOT
import os

# Create your models here.

media_dir = os.path.join(MEDIA_ROOT,"clothes/")

if not os.path.isdir(media_dir):
    os.mkdir(media_dir)


class Distributor(models.Model):
    distributor_name = models.CharField(unique=True)
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return f"Distributor: {self.distributor_name} | Email: {self.contact_email}"

class Brand(models.Model):
    brand_name = models.CharField(unique=True,max_length=50)
    distributor = models.OneToOneField(Distributor,on_delete=models.CASCADE)    
        
    def __str__(self):
        return f"Brand: {self.brand_name} | Distributor: {self.distributor.distributor_name}"

class Type_Clothe(models.Model):
    type_name = models.CharField(primary_key=True,max_length=20)
    
    def __str__(self):
        return self.type_name


class Clothes(models.Model):
    
    description = models.CharField(max_length=30)
    type_clothe = models.ForeignKey(Type_Clothe,null=True,on_delete=models.SET_NULL)
    gender = models.CharField(choices=[("F","Female"),("M","Male")],default="F")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    age = models.CharField(choices=[("C","Child"),("T","Teen"),("A","Adult")],default="T")
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to="clothes/",null=True)
    units = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Brand: {self.brand.brand_name} | Clothe type: {self.type_clothe.type_name} | Gender: {self.gender}"