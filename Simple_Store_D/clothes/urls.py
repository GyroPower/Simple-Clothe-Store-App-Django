from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    path("",views.HomeView.as_view(),name="Home"),
    path("products/F", views.ShowFemaleProducts.as_view(),name="products-F-All"),
    path("products/M", views.ShowMaleProducts.as_view(),name="products-M-All"),
    path("products/F/<str:type>",views.ShowFemaleProducts.as_view(), name="product-F"),
    path("products/M/<str:type>", views.ShowMaleProducts.as_view(),name="product-M"),
    path("products/<int:id>",views.ShowProduct.as_view(),name="detail-product")
]
# ] + static(settings.STATIC_URL,document=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# path("succes",succes,name="succes"),
# path("display",display_image,name="display")