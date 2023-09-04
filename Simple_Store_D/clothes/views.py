from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from django.views import View
from .repository import Male
from .repository import Female
from .repository import general
from django.conf import settings
from . import forms as my_forms

# Create your views here.


class HomeView(View):
    
    template_name = "main/main.html"
    
    def get(self,request):
        categorys_female,categorys_male = general.get_categorys_of_genders()
        
        latest_clothes_in_categorys_f = []
        latest_clothes_in_categorys_m = []
        
        for category in categorys_female:
            latest_clothes_in_categorys_f.append(general.get_latest_clothe_type(category.type_name,"F"))
        
        for category in categorys_male:
            latest_clothes_in_categorys_m.append(general.get_latest_clothe_type(category.type_name,"M"))

        return render(request,self.template_name,context={"category_F":categorys_female,
                                                          "category_M":categorys_male,
                                                          "items_for_slide_F":latest_clothes_in_categorys_f,
                                                          "items_for_slide_M":latest_clothes_in_categorys_m,
                                                          "M":"M",
                                                          "F":"F"})


class ShowFemaleProducts(View):
    
    template_name = "Products/products.html"
    
    def get(self,request:HttpRequest,type:str=""):
        categorys_female,categorys_male = general.get_categorys_of_genders()

        if type=="":
            clothes = Female.get_all_female_clothe()
        
        else:
            clothes = Female.get_all_type_clothe(type)

        return render(request,self.template_name,context={"clothes":clothes,
                                                    "path":"F",
                                                    "category_F":categorys_female,
                                                    "category_M":categorys_male,
                                                    "type":type})


class ShowProduct(View):
    
    template_name = "Products/product_detail.html"
    
    def get(self,request:HttpRequest,id):
        clothe = general.get_clothe(id=id)
        categorys_female,categorys_male = general.get_categorys_of_genders()
        
        color = []
        
        if clothe != None:
            color = clothe.color.all()
        
        
        
        return render(request,self.template_name,context={"clothe":clothe,
                                                          "category_F":categorys_female,
                                                          "category_M":categorys_male,
                                                          "color": color 
                                                          })

class ShowMaleProducts(View):
    
    template_name = "Products/products.html"
    
    def get(self,request:HttpRequest,type:str=""):
            
        categorys_female,categorys_male = general.get_categorys_of_genders()

        if type=="":
            
            clothes = Male.get_all_male_clothe()
        else:
            clothes = Male.get_all_type_clothe(type)
            
        return render(request,"Products/products.html",{"clothes":clothes,
                                                        "path":"M",
                                                        "category_F":categorys_female,
                                                        "category_M":categorys_male,
                                                        "type":type})    


