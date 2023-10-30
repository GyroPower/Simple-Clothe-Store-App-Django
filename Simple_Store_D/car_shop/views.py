from django.http import HttpRequest,JsonResponse
from django.shortcuts import redirect
from .car_shop import Car_Shop
from . import models
from .repository import car_shop as car_shop_repo
from clothes.repository import general

# Create your views here.

def get_clothe_id_color_id_size_id(string_id):
    count = 0
    clothe_id = ""
    color_id = ""
    size_id = ""
    for i in range(len(string_id)):
        if count < 1 and string_id[i] != "-":
            clothe_id +=string_id[i]
        elif 1==count<2 and string_id[i] != '-':
            color_id += string_id[i]
        elif 2==count<3 and string_id[i] != "-":
            size_id += string_id[i]
        else:
            count +=1
    
    return clothe_id,color_id,size_id

def add_to_car(request:HttpRequest,string_id):
    
    if request.user.is_authenticated:
        ids = get_clothe_id_color_id_size_id(string_id)
        
        car_shop = Car_Shop(request)
        
        
        
        clothe = general.get_clothe(ids[0])
        color = general.get_color(color_id=ids[1])
        size = general.get_size(size_id=ids[2])
        
        
        images = clothe.ColorImages.filter(color=color).first().images.all()
        
        image_url = ''
        for image in images.all():
            if image_url == '':
                image_url=image.image.url
                
            else:
                break
        
        
        
        car_shop.agregate_to_car(clothe,color,size,image_url)
        
        order_key = string_id 
        
        return JsonResponse(data = {"response":"V",
                                    "clothe_id":ids[0],
                                    "units":car_shop.car_shop[order_key]['units'],
                                    "color_id":car_shop.car_shop[order_key]['color_id'],
                                    "color" : car_shop.car_shop[order_key]['color'],
                                    "size_id" : car_shop.car_shop[order_key]['size_id'],
                                    "size": car_shop.car_shop[order_key]['size'],
                                    "desc":car_shop.car_shop[order_key]['description'],
                                    "price":car_shop.car_shop[order_key]['price'],
                                    "image":car_shop.car_shop[order_key]['img'],
                                    "items_id":list(car_shop.car_shop.keys())})
    
    return redirect('login')
        

def low_in_car(request:HttpRequest,string_id):
    
    ids = get_clothe_id_color_id_size_id(string_id)
    
    car_shop = Car_Shop(request)
    
    clothe = general.get_clothe(ids[0])
    color = general.get_color(color_id=ids[1])
    size = general.get_size(size_id=ids[2])
    
    car_shop.lower_clothe(clothe,color,size)
    key_order = str(clothe.id)+"-"+str(color.id) + "-"+str(size.id)
    
    if key_order in car_shop.car_shop.keys():
        data = {"response" : "V",
                "units":car_shop.car_shop[key_order]['units'],
                "price":car_shop.car_shop[key_order]['price']}
    else:
        data = {"response":"N"}
    
    return JsonResponse(data)

def delete_in_car(request:HttpRequest,string_id):
    
    ids = get_clothe_id_color_id_size_id(string_id)
    
    
    car_shop = Car_Shop(request)
        
    clothe = general.get_clothe(ids[0])
    color = general.get_color(color_id=ids[1])
    size = general.get_size(size_id=ids[2])
    
    car_shop.delete_clothe(clothe,color,size)
    clothe_id = str(clothe.id)
    
    return JsonResponse(data={"clothe_id":clothe_id})


def clear_car(request:HttpRequest):
    
    if request.user.is_authenticated:
        
        car_shop = Car_Shop(request)
        
        car_shop.delete_all()
        
        return JsonResponse(data={"response":"V"})
    
    return redirect('login')
    
def create_order(request:HttpRequest):
    
    if request.user.is_authenticated:
        
        car_shop = Car_Shop(request)
            
        response = car_shop_repo.create_order(car_shop,request.user)
        
        return JsonResponse(data=response)
    
    return redirect('login')