from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password



User = get_user_model()


def verify_user_credentials(email,password):
    
    user = User.objects.get(email=email)
    
    if user.check_password(password):
    
        return user
    else: 
        return None