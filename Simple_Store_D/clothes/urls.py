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
    path("products/<int:id>",views.ShowProduct.as_view(),name="detail-product"),
    path("colors",views.Show_Color.as_view(),name="Colors"),
    path("colors/<int:page_number>",views.get_paged_colors,name="get-paged-colors"),
    path("colors/add",views.Add_color.as_view(),name="add-color"),
    path("color/get",views.get_color_last,name="color-get-last"),
    path("color-image/add",views.Add_images_color_in_form.as_view()),
    path("color-image/update/<str:id>/<str:clothe_id>",views.Update_images_color_in_form.as_view()),
    path('color-image/last/<str:type_str>',views.get_last_images_color),
    path("images/add",views.Add_img.as_view()),
    path("image/delete/<int:id>",views.delete_img),
    path('images/update/<str:id>',views.edit_img.as_view()),
    path("get-list-img",views.last_item_in_session),
    path('delete-img-color/<str:id>',views.Add_images_color_in_form.as_view()),
    path('get-imgs-from-colorImage/<str:id>/<str:color_id>',views.get_images_of_imagesColor)
]
# ] + static(settings.STATIC_URL,document=settings.STATIC_ROOT)



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# path("succes",succes,name="succes"),
# path("display",display_image,name="display")