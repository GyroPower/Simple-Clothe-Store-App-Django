from genericpath import isfile
from django.forms import ImageField
from .. import models 
from PIL import Image 
import os 

# This are many funtions for the management of the models related of the clothe model and 
# the clothe model itself

def get_categorys_of_genders():
    # retrieves all the categorys in the clothes 
    female_categorys = models.Type_Clothe.objects.filter(clothes__gender="F").distinct("type_name")
    male_categorys = models.Type_Clothe.objects.filter(clothes__gender="M").distinct("type_name")
    return female_categorys,male_categorys

def get_latest_clothe_type(type_name:str,gender:str):
    # Retrieve the latest clothe in a type
    clothe = models.Clothes.objects.filter(type_clothe__type_name=type_name,gender=gender).latest("id")
    
    # And retrieves a resized image for a carousel to expose the most recents clothes 
    # of a type in a gender clothe
    slash = clothe.ColorImages.first().images.first().image.name.find("/")
    name = clothe.ColorImages.first().images.first().image.name[slash+1:]
    dot = name.find(".")
    
    new_name = name[:dot] + "_resized" + name[dot:]
    
    if not os.path.isfile("media/resized/"+new_name):
        
        new_path = "media/clothes_media/"+name
        
        
        image = Image.open(new_path)
        
        new_image = image.resize((810,1080))
        
        new_image.save("media/resized/"+new_name)
        
        
     
    
    return (clothe,"/media/resized/"+new_name)

def delete_img(id):
    # This delete a specific img
    try:
        image=models.image_for_clothe.objects.get(id=id)
        image.delete()
        return True
    except:
        return False
   
def get_clothe(id):
    # get a specific clothe instance
    try:
    
        return models.Clothes.objects.get(id=id)
    except:
        return None 
    
def get_color(color_id):
    # get a specific color instance
    return models.Colors.objects.get(id=color_id)


def get_last_color():
    # get the latest color instance
    return models.Colors.objects.latest("id")


# Mostly of the functions are very descriptive of what them does 

def get_size(size_id):
    return models.Sizes.objects.get(id=size_id)


def add_color(color_name:str,color_hexa:str):
    
    
    color=models.Colors.objects.create(color_name=color_name,color=color_hexa)
    
    if color:
        return True 
    else:
        return False

def get_all_colors():
    
    return models.Colors.objects.all()

def get_all_clothes():
    
    return models.Clothes.objects.all()


def add_color_to_clothe(colors):
    
    clothe = models.Clothes.objects.get(id=3)
    
    
    for color in colors:
        clothe.color.add(color)
        
        
    clothe.save()
    
    
def add_img(img):
    
    try:
        image = models.image_for_clothe.objects.create(image=img)
        
        image.save()
        
        return image
    except:
        return False 
    

def remove_unused_img(id):
    
    images_and_color=models.image_and_color_of_clothe.objects.filter(images__id=id)
    if images_and_color:
        clothe = models.Clothes.objects.filter(ColorImages__id=images_and_color.first().id)
        
        if clothe:
            return 
        
        images_and_color.delete()
        
        
    image = models.image_for_clothe.objects.filter(id=id)
    
    if image: 
        
        if os.path.isfile(image.first().image.path):
            os.remove(image.first().image.path)
        
        image.delete()
    
    return 

def last_image_in_session(id):
    return  models.image_for_clothe.objects.get(id=id)
    
    
def see_imgs(request):
    
    for image in models.image_for_clothe.objects.all():
        img = image.delete()
        
        
    request.session['img_items'] = []
    request.session.save()
    
def see_imgs_s():
    
    for image_color in models.image_and_color_of_clothe.objects.all():
        print(len(image_color.images.all()))
        

def create_images_color(imgs,color):
    
    
    
    image_color = models.image_and_color_of_clothe(color=color)
    image_color.save()
    
    # add the imgs to the newest imageColor instance
    for image in imgs:
        image_color.images.add(image)
        
    image_color.save()
    print(image_color.id)
    return image_color


def get_image(id):
    
    
    image = models.image_for_clothe.objects.get(id=id)
    
    return image

def update_img(id,image):
    
        
 
    to_update = models.image_for_clothe.objects.get(id=id)
    print(image)
    if to_update:
        
        if os.path.isfile(to_update.image.path):
            os.remove(to_update.image.path)
        
            to_update.image = image
            to_update.save()
            print(to_update.image.path)
            return True 
        
    return False        


def get_image_color(id):
    
    image_and_color = models.image_and_color_of_clothe.objects.filter(id=id)
    
    
    
    if image_and_color.first():
        return image_and_color.first()
    
    return None
    
def update_image_color(id,id_clothe,images,color):
    
    if id_clothe !='0':
        clothe = models.Clothes.objects.get(id=id_clothe)
        
        
        
        if not clothe.ColorImages.filter(id=id,color=color) and clothe.ColorImages.filter(color=color):
            
            return False 
        

        
        
    image_and_color= models.image_and_color_of_clothe.objects.get(id=id)
    
    if image_and_color:
        
        image_and_color.color = color 
        
        if len(images)>0:
            for img in images:
                if img not in image_and_color.images.all():
                    image_and_color.images.add(img)
                
        image_and_color.save()
        
        print("UPdated")
        return True
        
    return False
    

def delete_image_color(id):
    try:
        image_and_color = models.image_and_color_of_clothe.objects.get(id=id)
        
        image_and_color.delete()
        
        return True
    except:
        
        return False 
    


def get_images(id,color_id):
    
    clothe = models.Clothes.objects.filter(id=id)
    
    return clothe.first().ColorImages.filter(color__id=color_id).first().images.all()