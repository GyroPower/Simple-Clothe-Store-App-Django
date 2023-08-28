from django.db import models
from clothes.models import Colors
from clothes import models as clothes_models

from django.contrib.auth import get_user_model
# Create your models here.

user = get_user_model()


class Order_Clothe(models.Model):
    User = models.ForeignKey(user,on_delete=models.PROTECT)
    clothe = models.ForeignKey(clothes_models.Clothes,on_delete=models.PROTECT)
    color = models.ForeignKey(to=clothes_models.Colors,null=True,on_delete=models.SET_NULL)
    size = models.ForeignKey(to=clothes_models.Sizes,null=True,on_delete=models.SET_NULL)
    create_at = models.DateTimeField(auto_now_add=True)
    units = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.User.get_username()} | {self.clothe.description} | {self.create_at} | {self.units}"
    
class Order(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    order_data = models.ManyToManyField(Order_Clothe)
    total_to_pay = models.FloatField(default=0)    
   
    def __str__(self):
        return f"{self.pk} | {self.created_at} | {self.total}"
    
    @property
    def total(self):
        total = 0
        for order in self.order_data.all():
            total+= order.clothe.price * order.units
            
        return total

    

    