from django.contrib import admin
from .models import *
from django import forms
from . import forms as app_forms

forms.CheckboxSelectMultiple

# Register your models here.
class ColorClotheAdminInline(admin.TabularInline):

    read_only_fields = ("color_name","color_")
    model = Clothes.color.through
    extra = 1
    
    
class ColorAdmin(admin.ModelAdmin):
    list_display = ("color_name","color_")


class ClothesAdmin(admin.ModelAdmin):
    form = app_forms.ClothesModelForm
    
    inlines = [ColorClotheAdminInline]
    list_display = ("description","units","gender",'brand')
    
admin.site.register(Type_Clothe)
admin.site.register(Distributor)
admin.site.register(Brand)
admin.site.register(Clothes,ClothesAdmin)
admin.site.register(Sizes)
admin.site.register(Colors)