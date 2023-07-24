from django.urls import path 
from . import views

app_name = "car_shop"

urlpatterns = [
    path("car-shop/add/<int:clothe_id>",views.add_to_car,name="add"),
    path("car-shop/low/<int:clothe_id>",views.low_in_car,name="low"),
    path("car-shop/del/<int:clothe_id>",views.delete_in_car,name="delete"),
    path("car-shop/clear",views.clear_car,name="clear"),
    
]
