from django.contrib import admin
from .models import *
from django import forms
from . import forms as app_forms

forms.CheckboxSelectMultiple

# Register your models here.

    
class ColorAdmin(admin.ModelAdmin):
    list_display = ("color_name","color_")


class ClothesAdmin(admin.ModelAdmin):
    form = app_forms.ClothesModelForm
    
    list_display = ("description","units","gender",'brand')
    

class ImagesColorAdmin(admin.ModelAdmin):
    form = app_forms.ModelFormImagesColors
    
    


admin.site.register(Type_Clothe)
admin.site.register(Distributor)
admin.site.register(Brand)
admin.site.register(Clothes,ClothesAdmin)
admin.site.register(Sizes)
