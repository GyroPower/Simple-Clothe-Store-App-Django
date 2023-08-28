from django.contrib import admin 


class MyAdminSite(admin.AdminSite):
    site_header = "Simple Store in python"
    

admin_site = MyAdminSite(name="myadmin")