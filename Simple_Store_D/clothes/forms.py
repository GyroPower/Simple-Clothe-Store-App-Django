import os
from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.utils import ErrorList
from django.http import HttpRequest
from .widgets import MultiSelectColor, MultiSelectorImages,TextInputWithCounter,SelectColorRadioInput,ImagesColorSelector
from .models import Clothes,Colors, image_and_color_of_clothe,image_for_clothe
from colorfield.fields import ColorField
from .repository import general

from django_middleware_global_request import get_request




class ClothesModelForm(forms.ModelForm):
    
    class Meta:
        
        model = Clothes
        fields = '__all__'
        widgets = {
            'description' : TextInputWithCounter(max_lengh=20),
             
        }

    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        request = get_request()
        
        parent_id = 0
        if self.instance:
            parent_id = self.instance.id
        
        self.fields['ColorImages'].widget = ImagesColorSelector(parent_id=parent_id) 
        
        
        if not request.session.get('clothe_image_color_path'):
            request.session['clothe_image_color_path'] = request.path
        
        
        if request.session.get('img_items'):
            if request.session.get('clothe_image_color_path') and request.session.get('clothe_image_color_path') != request.path:
                for id in request.session.get('img_items'):
                    
                    general.remove_unused_img(id)
            
                print("Delete")
                request.session['img_items']=[] 
                request.session['clothe_image_color_path'] = []
                request.session.save()        
        
        

class ModelFormImagesColors(forms.ModelForm):
    
    class Meta:
        model = image_and_color_of_clothe
        fields = "__all__"
        widgets = {
            'images' : MultiSelectorImages(),
            "color" : SelectColorRadioInput(queryset=Colors.objects.all())
        }
        
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)
        request = get_request()
        self.fields['images'].widget.request = request 
        self.fields['color'].widget.queryset = Colors.objects.all()

    
        
    
class Form_images_color_added(forms.Form):
    
    images = forms.ModelMultipleChoiceField(queryset=image_for_clothe.objects.all(),widget=MultiSelectorImages())
    color = forms.ModelChoiceField(queryset=Colors.objects.all(),
                                            widget=SelectColorRadioInput(queryset=Colors.objects.all()))
    
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)
        request = get_request()
        self.fields['images'].widget.request = request 
        self.fields['color'].widget.queryset = Colors.objects.all()

          
        
        
class SimpleForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}))  
   

class ColorsForm(forms.Form):
    
        
    color = forms.ModelMultipleChoiceField(
        queryset=Colors.objects.all(),
        widget=MultiSelectColor(queryset=[])
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["color"].widget.queryset = Colors.objects.all() 
        
    
        
class AddImageForm(forms.Form):
    
    image_for = forms.ImageField(widget=forms.widgets.FileInput(attrs={"class":"form-control",
                                                                       "id":"image_for"}))


    
class AddColorForm(forms.Form):
    
    color_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control my-2",
                                      "id":"color_name"})
    )
    
    color_hexa = forms.CharField(
        widget=forms.widgets.TextInput(attrs={"type":"","data-jscolor":"{}",
                                              "class":"form-control my-2",
                                              "id":"color_hexa"})
    )