from django.http import HttpRequest,JsonResponse
from .car_shop import Car_Shop
from . import models
from .repository import car_shop as car_shop_repo
from clothes.repository import general

# Create your views here.

def add_to_car(request:HttpRequest,clothe_id):
    car_shop = Car_Shop(request)
    
    clothe = general.get_clothe(clothe_id)

    clothe_id = str(clothe.id)
    
    car_shop.agregate_to_car(clothe)
    
   
    return JsonResponse(data = {"clothe_id":clothe_id,
                                "units":car_shop.car_shop[clothe_id]['units'],
                                "desc":car_shop.car_shop[clothe_id]['description'],
                                "price":car_shop.car_shop[clothe_id]['price'],
                                "items_id":list(car_shop.car_shop.keys())})


def low_in_car(request:HttpRequest,clothe_id):
    
    car_shop = Car_Shop(request)
    
    clothe = general.get_clothe(clothe_id)
    
    car_shop.lower_clothe(clothe)
    clothe_id = str(clothe.id)
    
    
    return JsonResponse(data = {"units":car_shop.car_shop[clothe_id]['units'],
                                "price":car_shop.car_shop[clothe_id]['price']})

def delete_in_car(request:HttpRequest,clothe_id):
        
    car_shop = Car_Shop(request)
        
    clothe = general.get_clothe(clothe_id)
        
    car_shop.delete_clothe(clothe)
    clothe_id = str(clothe.id)
    
    return JsonResponse(data={"clothe_id":clothe_id})


def clear_car(request:HttpRequest):
    car_shop = Car_Shop(request)
    
    car_shop.delete_all()
    
    return JsonResponse(data={"response":"V"})
    
def create_order(request:HttpRequest):
    car_shop = Car_Shop(request)
    
    response = car_shop_repo.create_order(car_shop,request.user)
    
    return JsonResponse(data=response)