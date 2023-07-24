from django.contrib import admin
from .models import Brand,Clothes,Distributor,Type_Clothe
# Register your models here.

admin.site.register(Type_Clothe)
admin.site.register(Distributor)
admin.site.register(Brand)
admin.site.register(Clothes)