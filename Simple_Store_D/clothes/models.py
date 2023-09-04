from email.policy import default
from django.db import models
from colorfield.fields import ColorField
from .color_constants import colors
import os
from django.utils.html import format_html



# Create your models here.

class Sizes(models.Model):
    size = models.CharField(default="S")
    
    def __str__(self):
        return self.size

    class Meta:
        ordering = ['size']
        verbose_name_plural = "Sizes"

#This is for add the Sizes of clothes possibles
if len(Sizes.objects.all()) < 4:
    
    choices_list = [("S","Small"),("M","Medium"),("L","Large"),("XL","Xtra Large")]
    
    for choice in choices_list:
        
        Sizes.objects.create(size = choice[0]).save()


#This if for the media dir where it should save the images of the clothes 



class Distributor(models.Model):
    distributor_name = models.CharField(unique=True)
    contact_email = models.EmailField(unique=True)

    def __str__(self):
        return f"Distributor: {self.distributor_name} | Email: {self.contact_email}"

    class Meta:
        ordering = ['distributor_name']
        verbose_name_plural = "Distributors"
        
class Brand(models.Model):
    brand_name = models.CharField(unique=True,max_length=50)
    distributor = models.OneToOneField(Distributor,on_delete=models.CASCADE)    
        
    def __str__(self):
        return f"Brand: {self.brand_name} | Distributor: {self.distributor.distributor_name}"

    def name(self):
        return self.brand_name
    
    class Meta:
        ordering = ['brand_name']
        verbose_name_plural = "Brands"

class Type_Clothe(models.Model):
    type_name = models.CharField(primary_key=True,max_length=20)
    
    def __str__(self):
        return self.type_name

    class Meta: 
        ordering = ['type_name']
        verbose_name_plural = "Types of Clothes"

class Colors(models.Model):
    COLOR_PALETTE = [(value.hex_format(),key) for key,value in colors.items()]
    
    
    color_name= models.CharField(default="")
    color = ColorField(samples=COLOR_PALETTE)

    def color_(self):
        return format_html(
            '<div style="height: 20px; width: 20px; background-color: {};"></div>',
            self.color,
        )
    
    
    def __str__(self):
        return self.color_name

    class Meta:
        ordering = ['color_name']
        verbose_name_plural = "Colors"

class Clothes(models.Model):
    
    description = models.CharField(max_length=30)
    type_clothe = models.ForeignKey(Type_Clothe,null=True,on_delete=models.SET_NULL)
    gender = models.CharField(choices=[("F","Female"),("M","Male")],default="F")
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    age = models.CharField(choices=[("C","Child"),("T","Teen"),("A","Adult")],default="T")
    sizes = models.ManyToManyField(Sizes,blank=True)
    price = models.FloatField(null=True)
    units = models.IntegerField(default=0)
    color = models.ManyToManyField(Colors,blank=True)
    image = models.ImageField(upload_to="clothes_media/",null=True)
    
    def __str__(self):
        return f"{self.description} | {self.brand.brand_name} | {self.type_clothe.type_name} | Gender: {self.gender}"
    
    def brand_name(self):
        return self.brand.brand_name
    
    class Meta:
        ordering = ['brand']
        verbose_name_plural = "Clothes"
    

