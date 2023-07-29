from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect, render
from . import form as form_user
from car_shop.repository import orders
from .repository import auth_user as auth

# Create your views here.


def user_info(request:HttpRequest):
    
    if request.user.is_authenticated:
        clothes_in_order,order = orders.get_order_of_user(request.user)
        
        return render(request,template_name="User/User_info.html",context={"clothes_in_order":clothes_in_order,
                                                                           "order_of_user":order})
    else:
        redirect("login")
        

def login_user(request:HttpRequest):
    
    if request.method =="GET":
        form = form_user.LogUser()
        return render(request,template_name="User/login.html",context={"form":form})
    elif request.method == "POST":
        
        form = form_user.LogUser(request.POST)
        
        
        if form.is_valid():
             
            user = auth.verify_user_credentials(form.cleaned_data.get("email_user"),form.cleaned_data.get("password_user"))
            
            
            if user is not None:
                login(request,user)
            
                return redirect("Home")
        
        
        return render(request,template_name="User/login.html",context={"error":"Password or email invalid"})
        
        
def logout_user(request:HttpRequest):
    logout(request)
    
    return redirect("login")

def sigup_user(request:HttpRequest):
    
    if request.method == "GET":
        
        if not request.user.is_authenticated:
            
            return render(request,template_name="User/sigup.html",context={"":""})
        else:
            return redirect("user-info")
        
    elif request.method == "POST":
        form = form_user.SigupUser(request.POST)
        
        if form.is_valid():
            
            if form.check_password_equal():
                user = auth.save_user(form.cleaned_data.get("username"),
                                      form.cleaned_data.get("email_user"),
                                      form.cleaned_data.get("password_user_1"))
                
                if user:
                    return redirect("Home")
        
        else:
            
            return render(request,template_name="User/sigup.html",context={"Error":"Passwords are not the same"})