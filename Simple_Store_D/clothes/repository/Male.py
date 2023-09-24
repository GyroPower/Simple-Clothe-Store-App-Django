from .. import models

# This is the same as the Female.py funtions

def get_all_male_clothe():
    return models.Clothes.objects.filter(gender="M").all()


def get_all_type_clothe(type:str):
    type_clothe = models.Type_Clothe.objects.filter(type_name=type).first()
    return models.Clothes.objects.filter(gender="M",type_clothe=type_clothe).all()