from django.http import HttpRequest
from .car_shop import Car_Shop

def Total_to_pay(request:HttpRequest):
    total = 0
    
    if request.user.is_authenticated:
        for key, value in request.session["car_shop"].items():
            total += float(value['price'])
            
    return {"total_to_pay":total}