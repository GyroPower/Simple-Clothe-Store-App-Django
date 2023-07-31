from django import forms
from django.http import HttpRequest


class ChangePasswordUser(forms.Form):
    old_password = forms.CharField()
    password_1 = forms.CharField()
    password_2 = forms.CharField()
    
    def check_password_equal(self):
        return self.password_1 == self.password_2 

class LogUser(forms.Form):
    email_user = forms.EmailField()
    password_user = forms.CharField()
    

class SigupUser(forms.Form):
    username = forms.CharField()
    email_user = forms.EmailField()
    password_user_1 = forms.CharField()
    password_user_2 = forms.CharField()
    
    
    def check_password_equal(self):
        return self.password_user_1 == self.password_user_2
    
