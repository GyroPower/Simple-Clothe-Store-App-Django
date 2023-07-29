from django.urls import path 
from . import views

urlpatterns = [
    path("user/info",views.auth_user,name="user-info"),
    path("user/login",views.login_user,name="login"),
    path("user/logout",views.logout_user,name="logout"),
]
