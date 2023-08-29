from .. import models 
from PIL import Image 
import os 

def get_categorys_of_genders():
    female_categorys = models.Type_Clothe.objects.filter(clothes__gender="F").distinct("type_name")
    male_categorys = models.Type_Clothe.objects.filter(clothes__gender="M").distinct("type_name")
    return female_categorys,male_categorys

def get_latest_clothe_type(type_name:str,gender:str):
    clothe = models.Clothes.objects.filter(type_clothe__type_name=type_name,gender=gender).latest("id")
    
    
    slash = clothe.image.name.find("/")
    name = clothe.image.name[slash+1:]
    dot = name.find(".")
    
    new_name = name[:dot] + "_resized" + name[dot:]
    
    if not os.path.isfile("media/resized/"+new_name):
        
    
        image = Image.open(clothe.image.path)
        
        new_image = image.resize((1320,583))
        
        new_image.save("media/resized/"+new_name)
     
    
    return (clothe,"/media/resized/"+new_name)
    
def get_clothe(id):
    return models.Clothes.objects.get(id=id)

def get_color(color_id):
    return models.Colors.objects.get(id=color_id)

def get_size(size_id):
    return models.Sizes.objects.get(id=size_id)