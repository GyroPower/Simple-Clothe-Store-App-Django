from django.http import HttpRequest
from .. import models 
from .. import car_shop
from clothes.repository import general

def create_order(car_shop:car_shop.Car_Shop,user):

    # This create a order and a clothe order instance for every clothe in the order       

    order = models.Order()
    for key, value in car_shop.car_shop.items():
        
        clothe = general.get_clothe(id = value["clothe_id"])
        color = general.get_color(color_id=value['color_id'])
        size = general.get_size(size_id=value['size_id'])
        order_clothe =  models.Order_Clothe(clothe = clothe,color=color,size=size,User=user,units = value['units'])    
        order_clothe.save()
        order.save()
        order.order_data.add(order_clothe)

    order.total_to_pay = order.total
    order.save()
    
    car_shop.delete_all()
    
    return {"response":"V"}
