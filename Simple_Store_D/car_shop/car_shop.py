#this class represents a car shop 
#This takes care of the shoping part of the Store
from django.http import HttpRequest
from clothes import models 



class Car_Shop:
    
    def __init__(self,request:HttpRequest):
        
        self.request: HttpRequest = request 
        self.session = self.request.session 
        self.car_shop = self.session.get("car_shop")
        
        if not self.car_shop:
            self.car_shop = self.session["car_shop"] = {}
        
    
    def agregate_to_car(self,clothe:models.Clothes):
        # Adding the new clothe to shop in the car_shop
        clothe_id = str(clothe.id)
        if (clothe_id not in self.car_shop.keys()):
            self.car_shop[clothe_id] = {
                "clothe_id" : clothe_id,
                "description": clothe.description,
                "gender": clothe.gender,
                "age": clothe.age,
                "clothe_type": clothe.type_clothe.type_name,
                "price": round(clothe.price,2),
                "units": 1,
                "img": clothe.image.url
            }
        else:
            # if is alredy in the car_shop, just increments the units and the price of the 
            # clothe
            clothe_id = str(clothe.id)
             
            if clothe_id in self.car_shop:
                self.car_shop[clothe_id]['units'] += 1
                self.car_shop[clothe_id]['price'] =\
                    round(float(self.car_shop[clothe_id]["price"]) + clothe.price,2)
        
        # updating the car_shop and saving in the session
        self.save_car_shop()
    
    def save_car_shop(self):
        self.session['car_shop'] = self.car_shop
        self.session.modified = True
        
    def lower_clothe(self, clothe:models.Clothes):
        clothe_id = str(clothe.id)
        if clothe_id in self.car_shop:
            self.car_shop[clothe_id]['units'] -= 1
            # the \ tells to the next line is with the one before 
            self.car_shop[clothe_id]["price"] = \
                str(round(float(self.car_shop[clothe_id]["price"])- clothe.price,2))

            if self.car_shop[clothe_id]['units'] < 1:
                self.delete_clothe(clothe)
        
        self.save_car_shop()
        
    def delete_clothe(self, clothe:models.Clothes):
        
        clothe_id = str(clothe.id)
        
        if clothe_id in self.car_shop:
            del self.car_shop[clothe_id]
        self.save_car_shop()
            
    def delete_all(self):
        self.session["car_shop"] = {}
        self.session.modified = True 