from django import forms

class LogUser(forms.Form):
    email_user = forms.EmailField()
    password_user = forms.CharField()