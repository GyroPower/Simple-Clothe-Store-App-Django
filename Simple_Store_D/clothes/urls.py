from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path("",views.Home,name="Home"),
    path("products/F", views.show_Female_products,name="products-F-All"),
    path("products/M", views.show_Male_products,name="products-M-All"),
    path("products/F/<str:type>", views.show_Female_products, name="product-F"),
    path("products/M/<str:type>", views.show_Male_products,name="product-M"),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# path("succes",succes,name="succes"),
# path("display",display_image,name="display")