from django import forms
from django.http import HttpRequest
from django_middleware_global_request import get_request
from django.core.paginator import Paginator

from .repository import general




class MultiSelectColor(forms.widgets.CheckboxSelectMultiple):
    
    # This is a widget with a tested and learned how to customize it some way the widgets 
    # that django provide us
    
    template_name = "clothes/widgets/multi_color.html"
    
    input_type = 'checkbox'
    
    def __init__(self,queryset=[],paginate=10,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.queryset = queryset
        self.request = ""
        self.paginate = paginate
        
        
          
    def get_context(self, name: str, value, attrs):
        context = super().get_context(name,value,attrs)
        self.request = get_request()
        
        objetc_list = self.queryset
        
        self.session = self.request.session
        page_num = self.session.get("page_number")
        
        if not page_num:
            
            page_num = self.session['page_number'] = 1
        
        
        self.session['values'] = context['widget']['value']
        
        
        
        paginator = Paginator(objetc_list,self.paginate)
        
        page_obj = paginator.page(page_num) 
        if self.queryset:
            
            context['widget']['queryset'] = self.queryset
            context['widget']['page_obj'] = page_obj
            context['widget']['previous'] = page_num-1
            context['widget']['next'] = page_num + 1
        
        
        return context 
    
    
class ImagesColorSelector(forms.widgets.CheckboxSelectMultiple):
    
    template_name = 'clothes/widgets/images_color_overview.html'
    
    # This widget is for the creating of ColorImages or ImagesColor instance for a clothe
    # instance, it has js for dinamyc feedback of creating, updating and deleting actions
    
    def __init__(self,parent_id=0,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # The parent is the instance of the clothe who own's the ImageColor instance
        self.parent_id = parent_id 
    
    def get_context(self,*args,**kwargs):
        
        context = super().get_context(*args,**kwargs)
        
        imagesColorsInputsId = context['widget']['value']
        
        
        image_color_list = []
        
        # Pass in the context the many ImagesColor instances of the clothe
        if imagesColorsInputsId:
            for image_color_id in imagesColorsInputsId:
                
                image_color = general.get_image_color(image_color_id)

                
                
                if image_color:
                    images = []
                    # getting the imgs of the ImagesColor instance
                    for image in image_color.images.all():
                        
                        images.append([image.id,image.image.url])
                    
                    image_color_list.append([image_color.id,
                                             images,
                                             #this list is for the color info of the instance
                                             [image_color.color.color,image_color.color.color_name,image_color.color.id]])
        
        
    
        context['widget']['parent_id'] = self.parent_id
            
        
              
        context['widget']['images_color'] = image_color_list
        
        return context



class SelectColorRadioInput(forms.widgets.RadioSelect):
    
    # a custom widget to show different color options in a radioSelect field
    
    template_name = "clothes/widgets/radio_color.html"
    
    def __init__(self,queryset=[],*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.queryset = queryset
        
    
    def get_context(self,*args,**kwargs):
        context = super().get_context(*args,**kwargs)
        self.request = get_request()
        
        # This is for paginated all the instances to show it in a paginated mode in 
        # a html template
        
        page_num = self.request.session.get("page_number")
        objects_list = self.queryset
        
        #if there's not a page_number in session, it put in 1 
        if not page_num:
            page_num = self.request.session['page_number'] = 1
        
        #And start to paginate the queryset of colors
        paginator = Paginator(objects_list,10)
        #Get the list depending of the page
        page_obj = paginator.page(page_num)
        
        if self.queryset:
            #if is a query set we put in the context the page, and the indexs of the next and
            #previous
            context['widget']['page_obj'] = page_obj
            context['widget']['previous'] = page_num-1
            context['widget']['next'] = page_num+1
        
        return context
    
class MultiSelectorImages(forms.widgets.CheckboxSelectMultiple):
    template_name = "clothes/widgets/multi_images.html"
    
    # Custom widget to create imgs instances and add the id's as hidden inputs 
    # in the ColorImages widget for a clothe, adding js script for dinamyc feedback of 
    # creating and deleting actions
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.request = ""
        self.images_in_session = []
        
    
    def get_context(self, name: str, value, attrs):
        context = super().get_context(name,value,attrs)
        
        images_id_srcs = []
        
        for image_id in context['widget']['value']:
            image = general.last_image_in_session(image_id)
            images_id_srcs.append([image.id,image.image.url])
            
        
        if len(images_id_srcs)>0:
            context['widget']['queryset'] = images_id_srcs
            
        
        return context
        
        
    

class TextInputWithCounter(forms.widgets.TextInput):
    template_name = 'clothes/widgets/custom_text_input.html'
    
    def __init__(self,max_lengh=None,*args,**kwargs):
        self.max_length = max_lengh
        super().__init__(*args,**kwargs)
        
    def get_context(self,name,value,attrs=None):
        context = super().get_context(name,value,attrs)
             
        if self.max_length:
            context['max_length'] = self.max_length
            
        return context 
    
    
        


 
    