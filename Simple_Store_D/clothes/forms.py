from typing import Any
from django import forms
from .widgets import MultiSelectColor,TextInputWithCounter
from .models import Clothes,Colors

forms.MultipleChoiceField
forms.CheckboxSelectMultiple

class ClothesModelForm(forms.ModelForm):
    
    class Meta:
        
        model = Clothes
        fields = '__all__'
        widgets = {
            'description' : TextInputWithCounter(max_lengh=20),
            
        }
    
    
  
   
        