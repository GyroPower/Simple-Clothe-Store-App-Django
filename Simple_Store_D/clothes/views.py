import json
import re
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.views import View
from pydantic import Json
from .repository import Male
from .repository import Female
from .repository import general
from django.conf import settings
from . import forms as my_forms
from .widgets import MultiSelectColor
from django.core.paginator import Paginator

# Create your views here.


# mostly of the urls it's for admin actions, to add images and colors for the clothes
# and for that allow the user to use it it has to be an admin or staff


# Some views add lists and add numbers of id's instances in those lists, this lists are store
# in the session of the user, this is just for the admin, this is made it 
# for make easier the retrieve of some info in some endpoints.
# This ids are for retrieve the most recent created or updated instance of a model that is
# linked in a instace of the clothe model

class HomeView(View):
    
    template_name = "main/main.html"
    
    def get(self,request):
        
        # this view retrieve the most recent added clothes in diferents categoys for female
        # and male clothes
        
        categorys_female,categorys_male = general.get_categorys_of_genders()
        
        latest_clothes_in_categorys_f = []
        latest_clothes_in_categorys_m = []
        
            
        for category in categorys_female:
            latest_clothes_in_categorys_f.append(general.get_latest_clothe_type(category.type_name,"F"))
        
        for category in categorys_male:
            latest_clothes_in_categorys_m.append(general.get_latest_clothe_type(category.type_name,"M"))

        return render(request,self.template_name,context={"category_F":categorys_female,
                                                          "category_M":categorys_male,
                                                          "items_for_slide_F":latest_clothes_in_categorys_f,
                                                          "items_for_slide_M":latest_clothes_in_categorys_m,
                                                          "M":"M",
                                                          "F":"F"})


class ShowFemaleProducts(View):
    
    # This views gives only female clothe, and it shares a funtion call to retrieve the 
    # categorys in the navbar for the male and female clothe
    
    template_name = "Products/products.html"
    
    def get(self,request:HttpRequest,type:str=""):
        categorys_female,categorys_male = general.get_categorys_of_genders()

        if type=="":
            clothes = Female.get_all_female_clothe()
        
        else:
            clothes = Female.get_all_type_clothe(type)

        return render(request,self.template_name,context={"clothes":clothes,
                                                    "path":"F",
                                                    "category_F":categorys_female,
                                                    "category_M":categorys_male,
                                                    "type":type})


class ShowProduct(View):
    
    # This view gives details of a specific clothe and the html template with js 
    # allow to the user if is authenthicated to put in the shopping cart
    
    template_name = "Products/product_detail.html"
    
    def get(self,request:HttpRequest,id):
        clothe = general.get_clothe(id=id)
        categorys_female,categorys_male = general.get_categorys_of_genders()
        
        color = []
        colorImages = []
        images = []
        if clothe != None:
            colorImages = clothe.ColorImages.all()
            
            for color_image in colorImages.all():
                color.append(color_image.color)
                
            for image in colorImages.first().images.all():
                images.append(image.image.url)    
                #print(image.image.url)
               
        
            
        
        
        return render(request,self.template_name,context={"clothe":clothe,
                                                          "category_F":categorys_female,
                                                          "category_M":categorys_male,
                                                          "colors": color,
                                                          "images":images
                                                          })


class ShowMaleProducts(View):
    
    template_name = "Products/products.html"
    
    # Same as the ShowFemaleProducts
    
    def get(self,request:HttpRequest,type:str=""):
            
        categorys_female,categorys_male = general.get_categorys_of_genders()

        if type=="":
            
            clothes = Male.get_all_male_clothe()
        else:
            clothes = Male.get_all_type_clothe(type)
            
        return render(request,"Products/products.html",{"clothes":clothes,
                                                        "path":"M",
                                                        "category_F":categorys_female,
                                                        "category_M":categorys_male,
                                                        "type":type})    


class Show_Color(View):
    
    # This is a test view for learning how to use forms and widgets
    
    template_name = "Colors/Colors.html"
    
    form_class = my_forms.ColorsForm
    
    def get(self,request:HttpRequest):
        
        
        
        categorys_female,categorys_male = general.get_categorys_of_genders()
        
        form = self.form_class()



        return render(request,self.template_name,{"category_F":categorys_female,
                                                  "category_M":categorys_male,
                                                  "form":form})
        
    
    def post(self,request:HttpRequest):
        
        form = self.form_class(request.POST)
        
        if form.is_valid():
            clothe = general.add_color_to_clothe(form.cleaned_data.get("colors"))
            
        return redirect("Colors")
    

class Add_color(View):
    
    # This is for a admin or staff to add a color if not exists
    
    template_name = "Colors/add_color.html"
    form_class = my_forms.AddColorForm
    
    def get(self,request:HttpRequest):
        
        if request.user.is_authenticated:
            form = self.form_class()
                
            return render(request,self.template_name,{"form":form})
    
    def post(self,request:HttpRequest):
        
        if request.user.is_authenticated:
            form = self.form_class(request.POST)
            
            if form.is_valid():
                
                if general.add_color(form.cleaned_data.get("color_name"),
                                    form.cleaned_data.get("color_hexa")):
                            
                    return JsonResponse(data={"response":"V"})
            
            
            return JsonResponse(data={"response":"N"})


def get_color_last(request:HttpRequest):
    # This retrieves a Json to add the last color created in a form with a fetch js call
    
    if request.user.is_authenticated:
        color = general.get_last_color()
        
        return JsonResponse(data={"color_id":color.id,
                                "color":color.color,
                                "color_name":color.color_name})
        


def get_paged_colors(request:HttpRequest,page_number):
    # This if for dinamically get a paged list of the colors in a form    
    if request.user.is_authenticated:
        
        objetc_list = general.get_all_colors()

        # Assinging the current page_number
        request.session['page_number'] = page_number
        
        #ANd paginate again depending of the page_number
        paginator = Paginator(objetc_list,10)
        
        page_obj = paginator.page(page_number)
        
        
        page_elements = []
        
        #Put in the info in a Json format for the js funtion get the info and display the 
        #corrent html for it
        for element in page_obj:
            page_elements.append({"color_id":element.id,
                                "color_name":element.color_name,
                                "color_hex":element.color})
        
        return JsonResponse(data={"page_objs":page_elements,
                                "page_number":page_number,
                                "pages_number":paginator.num_pages,
                                "values":request.session.get("values")})
        
        

class Add_img(View):
    
    # This is for add a image in a ColorImage model instance, this instance if for
    # add diferent color a clothe could have, and for direfent color can have different 
    # images to see how is the clothe
    
    template_name="Colors/add_image.html"
    
    form_class = my_forms.AddImageForm
    
    def get(self,request:HttpRequest):
    
        if request.user.is_authenticated:    
            form = self.form_class()
            
            
            return render(request,self.template_name,context={"form":form})
        
    def post(self,request:HttpRequest):
    
        if request.user.is_authenticated:
                    
            form = self.form_class(request.POST,request.FILES)
            
            
            if form.is_valid():
                img  = form.cleaned_data.get("image_for")
                image = general.add_img(img=img)
                
                if image:
        
                    if not request.session.get("img_items"):
                        request.session['img_items'] = []
                    
                    request.session['img_items'].append(str(image.id))
                    request.session.save() 
        
                    return JsonResponse(data={"response":"v"})
                
        
            
            return JsonResponse(data={"response":"n"})
                

class Update_images_color_in_form(View):
    # This is for update a img in a ColorImage instance, the img is a model too
    
    template_name = "Colors/images_color_for_form.html"
    
    form_class = my_forms.ModelFormImagesColors
    
    def get(self,request:HttpRequest,id,clothe_id):
        
        if request.user.is_authenticated:
            
            images_color = general.get_image_color(id=id)
            form = self.form_class(instance=images_color)
            update = id
        
            return render(request,self.template_name,context={'form':form,
                                                              "update":update,
                                                              "clothe_id":clothe_id})
    
    def post(self,request:HttpRequest,id,clothe_id):
        
        if request.user.is_authenticated:
            form = self.form_class(request.POST)
        
            if form.is_valid():
                image_color = general.update_image_color(id,clothe_id,form.cleaned_data.get('images'),form.cleaned_data.get('color'))
                
                if not request.session.get('image_color_session_update'):
                    request.session['image_color_session_update'] = []
                        
                            
                color_images = set(request.session.get('image_color_session_update'))
                
                color_images.discard(clothe_id)
                
                request.session['image_color_session_update'].append(id)
                request.session.save()
                
                
                if image_color:
                    return JsonResponse(data={'response':"v"})

                
                
                return JsonResponse(data={'response':'r',
                                          "errors":'The clothe alredy have the color you wanna add'})
            
            return JsonResponse(data={'response':'n',
                                      "errors":form.errors})
        
        
class Add_images_color_in_form(View):
    
    # Clothes can have multiple colors, and those colors could have different imgs to show 
    # how it looks the clothe, this views is for add a ColorImage instance to a clothe instance
    # and it has a method for deleting a instance of the ColorImage model
    template_name = "Colors/images_color_for_form.html"
    
    form_class = my_forms.ModelFormImagesColors
    
    def get(self,request:HttpRequest):

        if request.user.is_authenticated:
        
            form = self.form_class()
            update=False 
            
            
            return render(request,self.template_name,context={"form":form,
                                                              "update":update})
            
        
    def post(self,request:HttpRequest):
        
        if request.user.is_authenticated:
            form = self.form_class(request.POST,request.FILES)
            
            if form.is_valid():
                            
                images_color = general.create_images_color(form.cleaned_data.get("images"),
                                            form.cleaned_data.get("color"))
                
                # This is for the adding part of the ColorImage instance's id's list in the admin session
                if not request.session.get('image_color_session_add'):
                    request.session['image_color_session_add'] = []

                request.session['image_color_session_add'].append(images_color.id)
                request.session.save()
                
                
                
                return JsonResponse(data={"response":"v"})
            
            return JsonResponse(data={"response":"n",'errors':form.errors})
        
    
        
    def delete(self,request:HttpRequest,id):
    
        if request.user.is_authenticated:
            color_image = general.delete_image_color(id)
            
            if color_image:
                return JsonResponse(data={'response':'v'})
            
            return JsonResponse(data={'response':'n',
                                      'errors':'Something went wrong, try again later'})

    
def last_item_in_session(request:HttpRequest):
    
    # This is for retrieve the last img added, to add in a form for the creation of a 
    # ColorImage instance
    
    if request.user.is_authenticated:
        imgs = request.session.get("img_items")
        
        if imgs:
                
            
            last_img_in_session = general.last_image_in_session(imgs[len(imgs)-1])
            
            
            return JsonResponse(
                data={"response":'v',
                    "id":last_img_in_session.id,
                    "path":last_img_in_session.image.url}
            )

        return JsonResponse(data={'response':'n'})


class edit_img(View):
    
    # This is for img to be updated in a ColorImage instance
    
    template_name = 'Colors/add_image.html'
    
    form_class = my_forms.AddImageForm
    
    def get(self,request:HttpRequest,id):
        
        if request.user.is_authenticated:
        
            image = general.get_image(id)
            form = self.form_class()
        
            return render(request,self.template_name,context={"form":form,
                                                            "image":image.image.url,
                                                            "id":id})
            
    
    def post(self,request:HttpRequest,id):
        
        if request.user.is_authenticated:
            form = self.form_class(request.POST,request.FILES)
        
            if form.is_valid():
                response = general.update_img(id,form.cleaned_data.get('image_for'))
                
                if response:
                    
                    if not request.session.get("img_items"):
                        request.session['img_items'] = []
                    
                    request.session['img_items'].append(str(id))
                    request.session.save() 
                else: 
        
                    return JsonResponse(data={"response":"n"})
            
            print("response")
            return JsonResponse(data={'response':'v'})


def delete_img(request:HttpRequest,id):
    # This view is just for deleting a img 
    
    
    if request.user.is_authenticated:  
        if request.method == "DELETE":      
            response = general.delete_img(id)
            
            if response:
                
                return JsonResponse(data={"response":"v",
                                        "id":id})
                
            return JsonResponse(data={'response':'n',
                                    'errors':'Something went wrong, try again later'})

            
def get_last_images_color(request:HttpRequest,type_str):
    
    # Retrieves a Json with info of the last instance added in the list session,
    # there are two, for the added (the created ones) and the updates instances
    
    if request.user.is_authenticated:
        image_color_session = request.session.get('image_color_session_'+type_str)
        
        if image_color_session:
            image_color = general.get_image_color(image_color_session[len(image_color_session)-1])
            
            if image_color:
                
                image_list = []
                
                image_color
                
                for image in image_color.images.all():
                    image_list.append(image.image.url)
                
                return JsonResponse(data={"response":'v',
                                        'id':image_color.id,
                                        "images_src":image_list,
                                        "color":image_color.color.color,
                                        "color_name":image_color.color.color_name,
                                        "color_id":image_color.color.id})

        return JsonResponse(data={'response':"n"})





def get_images_of_imagesColor(request:HttpRequest,id,color_id):
    
    # This return a Json with a list of the src's of the imgs of a ColorImage instance
    # when a user whats to see the imgs of the color for a clothe, this is called
    
    images_src = []
    
    images = general.get_images(id,color_id)
    
    for image in images:
        images_src.append(image.image.url)
        
    
    return JsonResponse(data={'response':'v',
                              'imgs_src':images_src})