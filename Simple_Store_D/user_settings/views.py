from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render

from clothes.repository import general
from . import form as form_user
from car_shop.repository import orders
from .repository import auth_user as auth
from django.contrib.auth import get_user_model
from django.views import View  
from clothes.repository import Male
from clothes.repository import Female


# Create your views here.

class UserInfo(View):
    
    def get(self,request:HttpRequest):
        if request.user.is_authenticated:
            categorys_female,categorys_male = general.get_categorys_of_genders()
            clothes_in_order, order = orders.get_order_of_user(request.user)
            
            return render(request,template_name="User/User_info.html",context={"clothes_in_order":clothes_in_order,
                                                                            "order_of_user":order,
                                                                            "category_F":categorys_female,
                                                                            "category_M":categorys_male})
        else:
            return redirect("login")
        

class LoginUser(View):
    
    form_class = form_user.LogUser
    template_name = "User/login.html"


    def get(self,request:HttpRequest):
        if not request.user.is_authenticated:
            categorys_female,categorys_male = general.get_categorys_of_genders()
            
            return render(request,self.template_name,{"category_F":categorys_female,
                                                    "category_M":categorys_male})
        return redirect("user-info")

    
    def post(self,request:HttpRequest):
        form = self.form_class(request.POST)
        error = "write a valid email"
        
        if form.is_valid():
            user = auth.verify_user_credentials(form.cleaned_data.get("email_user"),form.cleaned_data.get("password_user"))
            
            
            if user is not None:
                login(request,user)
            
                return redirect("Home")
        
            error= "Password or email invalid"
        
        return render(request,self.template_name,context={"error":error})
        

class LogOutUser(View):
    
    def get(self,request:HttpRequest):
        logout(request)
        
        return redirect("login")


class SigUpUser(View):
 
    template_name="User/sigup.html"
    form_class = form_user.SigupUser

    
    def get(self,request:HttpRequest):
        if not request.user.is_authenticated:
            categorys_female,categorys_male = general.get_categorys_of_genders()
            
            return render(request,self.template_name,context={"category_F":categorys_female,
                                                                "category_M":categorys_male})
        else:
            return redirect("user-info")


    def post(self,request:HttpRequest):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            if form.check_password_equal():
                user = auth.save_user(form.cleaned_data.get("username"),
                                      form.cleaned_data.get("email_user"),
                                      form.cleaned_data.get("password_user_1"))
            
                if user:
                    return redirect("Home")
        else:
            return render(request,self.template_name,context={"Error":"Passwords are not the same"})


class ChangePasswordUser(View):
    
    template_name = "User/change_password.html"
    form_class = form_user.FormChangePasswordUser
    
    
    def get(self,request:HttpRequest):
        
        if request.user.is_authenticated:
            categorys_female,categorys_male = general.get_categorys_of_genders()
            
            return render(request,self.template_name,context={"category_F":categorys_female,
                                                    "category_M":categorys_male})

        return redirect("login")
    
    
    def post(self,request:HttpRequest):
        
        if request.user.is_authenticated:
            categorys_female,categorys_male = general.get_categorys_of_genders()
            
            form = self.form_class(request.POST) 
            
            error = "Passwords are not equals"
            
            if form.is_valid() and form.cleaned_data.get("password_1") == form.cleaned_data.get('password_2'):
                
                user = auth.change_password(request.user.id,
                                            form.cleaned_data.get("old_password"),
                                            form.cleaned_data.get("password_1"))
                error = "Password incorrect"
                
                
                if user:
                    
                    return redirect("Home")
                
            return render(request,self.template_name,context={"error":error,
                                                              "category_F":categorys_female,
                                                              "category_M":categorys_male})
                        