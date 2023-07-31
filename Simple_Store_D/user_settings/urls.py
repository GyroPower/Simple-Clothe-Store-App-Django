from django.urls import path 
from . import views

urlpatterns = [
    path("user/info",views.user_info,name="user-info"),
    path("user/login",views.login_user,name="login"),
    path("user/logout",views.logout_user,name="logout"),
    path("user/sigup",views.sigup_user,name="sigup"),
    path("user/change-password",views.change_password_user,name="change_password")
]
