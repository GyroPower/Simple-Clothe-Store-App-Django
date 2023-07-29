from django.http import HttpRequest
from .. import models 
from .. import car_shop
from clothes.repository import general

def create_order(car_shop:car_shop.Car_Shop,user):
    
    try:
        order = models.Order()
        for key, value in car_shop.car_shop.items():
            clothe = general.get_clothe(id = value["clothe_id"])
            order_clothe =  models.Order_Clothe(clothe = clothe,User=user,units = value['units'])    
            order_clothe.save()
            order.save()
            order.order_data.add(order_clothe)

        order.total_to_pay = order.total
        order.save()
        
        car_shop.delete_all()
        
        return {"response":"V"}
    except:
        return {"response":"N"}