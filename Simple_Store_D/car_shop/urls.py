from django.urls import path 
from . import views

app_name = "car_shop"

urlpatterns = [
    path("car-shop/add/<str:string_id>",views.add_to_car,name="add"),
    path("car-shop/low/<str:string_id>",views.low_in_car,name="low"),
    path("car-shop/del/<str:string_id>",views.delete_in_car,name="delete"),
    path("car-shop/clear",views.clear_car,name="clear"),
    path("car-shop/order",views.create_order,name="create-order")
]
