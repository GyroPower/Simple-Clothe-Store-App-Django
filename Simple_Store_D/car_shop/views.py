from django.http import HttpRequest,JsonResponse
from django.shortcuts import render
from .car_shop import Car_Shop
from clothes import models as models_clothes
from . import models
from django.shortcuts import redirect 
from clothes.repository import Female, Male 

# Create your views here.

def add_to_car(request:HttpRequest,clothe_id):
    car_shop = Car_Shop(request)
    
    clothe = models_clothes.Clothes.objects.get(id=clothe_id)

    clothe_id = str(clothe.id)
    
    car_shop.agregate_to_car(clothe)
    
   
    return JsonResponse(data = {"clothe_id":clothe_id,
                                "units":car_shop.car_shop[clothe_id]['units'],
                                "desc":car_shop.car_shop[clothe_id]['description'],
                                "price":car_shop.car_shop[clothe_id]['price'],
                                "items_id":list(car_shop.car_shop.keys())})


def low_in_car(request:HttpRequest,clothe_id):
    
    car_shop = Car_Shop(request)
    
    clothe = models_clothes.Clothes.objects.get(id=clothe_id)
    
    car_shop.lower_clothe(clothe)
    clothe_id = str(clothe.id)
    
    
    return JsonResponse(data = {"units":car_shop.car_shop[clothe_id]['units'],
                                "price":car_shop.car_shop[clothe_id]['price']})

def delete_in_car(request:HttpRequest,clothe_id):
        
    car_shop = Car_Shop(request)
        
    clothe = models_clothes.Clothes.objects.get(id=clothe_id)
        
    car_shop.delete_clothe(clothe)
    clothe_id = str(clothe.id)
    
    return JsonResponse(data={"clothe_id":clothe_id})


def clear_car(request:HttpRequest):
    car_shop = Car_Shop(request)
    
    car_shop.delete_all()
    
    return JsonResponse(data={"response":"V"})
    
def create_order(request:HttpRequest):
    car_shop = Car_Shop(request)
    order = models.Order()
    for key, value in car_shop.car_shop.items():
        clothe = models_clothes.Clothes.objects.get(id = value["clothe_id"])
        order_clothe =  models.Order_Clothe(clothe = clothe,User=request.user,units = value['units'])    
        order_clothe.save()
        order.save()
        order.order_data.add(order_clothe)

    order.total_to_pay = order.total
    
    
    car_shop.delete_all()
    
    return JsonResponse(data={"response":"V"})