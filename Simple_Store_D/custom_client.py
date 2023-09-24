from django.test import Client
from django.contrib.auth.models import User

class Custom_Client(Client):
    
    #A custom client instance to login with the email for tests
    def login_by_email(self,email,password):
        
        user = User.objects.get(email=email)
        
        if user.check_password(password):
            self._login(user)
            return True 
        
        return False