from django.http import HttpRequest
from .. import models 

def get_order_clothes_of_an_order(order_id):
    clothes_orders = models.Order_Clothe.objects.filter(order__id=order_id)
    
    return clothes_orders.all()

def get_order_of_user(User):
    orders = models.Order.objects.filter(order_data__User=User).all()
    
    orders_list = []
    for order in orders:
        if order not in orders_list:
            orders_list.append(order)
    
    
    clothes_in_order = {}
    
    for order in orders_list:
    
        clothes_in_order[order.pk] = []
        clothes_in_order[order.pk] +=(get_order_clothes_of_an_order(order.pk)) 
    
    
    return clothes_in_order,orders_list        
    