from django import forms



class MultiSelectColor(forms.widgets.CheckboxSelectMultiple):
    template_name = "clothes/widgets/multi_color.html"
    
    input_type = 'checkbox'
    
    def __init__(self,queryset,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.queryset = queryset
        
    def get_context(self, name: str, value, attrs):
        context = super().get_context(name,value,attrs)

        if self.choices:
            context['widget']['queryset'] = self.queryset
         
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
    
    
        


 
    