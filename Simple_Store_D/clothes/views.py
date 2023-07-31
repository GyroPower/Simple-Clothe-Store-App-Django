from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from .repository import Male
from .repository import Female
from django.conf import settings

# Create your views here.


def Home(request:HttpRequest):
    
    
    categorys_female = Female.get_all_female_clothe()
    categorys_male = Male.get_all_male_clothe()
    return render(request,"main/main.html",{"category_F":categorys_female,"category_M":categorys_male,"path":"home"})

def show_Female_products(request:HttpRequest,type:str=""):
    categorys_female = Female.get_all_female_clothe()
    categorys_male = Male.get_all_male_clothe()

        
    if type=="":
        clothes = Female.get_all_female_clothe()
    
    else:
        clothes = Female.get_all_type_clothe(type)
   
    
    return render(request,"Products/products.html",{"clothes":clothes,
                                                    "path":"F",
                                                    "category_F":categorys_female,
                                                    "category_M":categorys_male,
                                                    "type":type})

def show_Male_products(request:HttpRequest,type:str=""):
    
    categorys_female = Female.get_all_female_clothe()
    categorys_male = Male.get_all_male_clothe()

    if type=="":
        
        clothes = Male.get_all_male_clothe()
    else:
        clothes = Male.get_all_type_clothe(type)
        
    return render(request,"Products/products.html",{"clothes":clothes,
                                                    "path":"F",
                                                    "category_F":categorys_female,
                                                    "category_M":categorys_male,
                                                    "type":type})
