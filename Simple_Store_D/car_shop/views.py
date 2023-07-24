from django.http import HttpRequest,JsonResponse
from django.shortcuts import render
from .car_shop import Car_Shop
from clothes import models as models_clothes
from . import models
from django.shortcuts import redirect 
# Create your views here.

def add_to_car(request:HttpRequest,clothe_id):
    car_shop = Car_Shop(request)
    
    clothe = models_clothes.Clothes.objects.get(id=clothe_id)

    clothe_id = str(clothe_id)
    
    car_shop.agregate_to_car(clothe)
    
    
    return JsonResponse(data = {"units":car_shop.car_shop[clothe_id]['units']})


def low_in_car(request:HttpRequest,clothe_id):
    
    car_shop = Car_Shop(request)
    
    clothe = models_clothes.Clothes.objects.get(id=clothe_id)
    
    car_shop.lower_clothe(clothe)
    clothe_id = str(clothe_id)
    
    print(car_shop.car_shop[clothe_id]['units'])
    
    return JsonResponse(data = {"units":car_shop.car_shop[clothe_id]['units']})

def delete_in_car(request:HttpRequest,clothe_id):
        
    car_shop = Car_Shop(request)
        
    clothe = models_clothes.Clothes.objects.get(id=clothe_id)
    
    clothe_id = str(clothe_id)
        
    car_shop.delete_clothe(clothe)
    
 
    return JsonResponse()


def clear_car(request:HttpRequest,path="",type=""):
    car_shop = Car_Shop(request)
    
    car_shop.delete_all()
    
    return JsonResponse()
    
def create_order(request:HttpRequest,path):
    order = models.Order()
    for key, value in request.session["car_shop"].items():
        clothe = models_clothes.Clothes.objects.get(id = value["clothe_id"])
        order_clothe =  models.Order_Clothe(clothe = clothe,units = value['units'])    

        order.order_data.add(order_clothe)

        order_clothe.save()
        
    order.total_to_pay = order.total
    order.save()
    
    return redirect("product-"+path)