from .. import models

def get_all_female_clothe():
    return models.Clothes.objects.filter(gender="F").all()

def get_all_type_clothe(type:str):
    clothe_type = models.Type_Clothe.objects.filter(type_name=type).first()
    
    return models.Clothes.objects.filter(gender="F",type_clothe=clothe_type).all()