from django.db import models
from clothes import models as clothes_models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Order_Clothe(models.Model):
    User = models.ForeignKey(User,on_delete=models.PROTECT)
    clothe = models.ForeignKey(clothes_models.Clothes,on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    units = models.IntegerField(default=1)
    
    
class Order(models.Model):
    
    created_at = models.DateTimeField(auto_now_add=True)
    order_data = models.ManyToManyField(Order_Clothe)
    total_to_pay = models.FloatField(default=0)    
   
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        total = 0
        for order in self.order_data.all():
            total+= order.clothe.price * order.units
            
        return total

    

    