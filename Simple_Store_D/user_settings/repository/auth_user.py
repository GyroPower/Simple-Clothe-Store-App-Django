from django.contrib.auth import get_user_model
from django.contrib.auth.models import User 


User_model = get_user_model()


def verify_user_credentials(email,password):
    
    user = User_model.objects.get(email=email)
    
    if user.check_password(password):
    
        return user
    else: 
        return None
    

def save_user(username="",email="",password=""):
    
    try:
        user = User.objects.create_user(username,email,password)
    
        user.save()
        
        return True 
    except:
        return False