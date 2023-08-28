from .. import models 

def get_categorys_of_genders():
    female_categorys = models.Type_Clothe.objects.filter(clothes__gender="F").distinct("type_name")
    male_categorys = models.Type_Clothe.objects.filter(clothes__gender="M").distinct("type_name")
    return female_categorys,male_categorys

def get_latest_clothe_type(type:str,gender:str):
    return models.Clothes.objects.filter(type_clothe__type_name=type,gender=gender).filter().latest("id")
    
def get_clothe(id):
    return models.Clothes.objects.get(id=id)

def get_color(color_id):
    return models.Colors.objects.get(id=color_id)

def get_size(size_id):
    return models.Sizes.objects.get(id=size_id)