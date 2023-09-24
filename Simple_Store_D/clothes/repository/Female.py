from .. import models

def get_all_female_clothe():
    # This retrieve all the female clothe in order of the most recent 
    return models.Clothes.objects.filter(gender="F").all()

def get_all_type_clothe(type:str):
    # This retrieve all the female clothe of one type 
    clothe_type = models.Type_Clothe.objects.filter(type_name=type).first()
    
    return models.Clothes.objects.filter(gender="F",type_clothe=clothe_type).all()