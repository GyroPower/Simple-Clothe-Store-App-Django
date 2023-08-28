from django.urls import path 
from . import views

urlpatterns = [
    path("user/info",views.UserInfo.as_view(),name="user-info"),
    path("user/login",views.LoginUser.as_view(),name="login"),
    path("user/logout",views.LogOutUser.as_view(),name="logout"),
    path("user/sigup",views.SigUpUser.as_view(),name="sigup"),
    path("user/change-password",views.ChangePasswordUser.as_view(),name="change_password")
]
