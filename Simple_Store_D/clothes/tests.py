from django.test import TestCase
from clothes import models 
from django.core.files import File 
from django.test import Client 
import os 
from Simple_Store_D.settings import BASE_DIR


# Create your tests here.

# def populate_db_of_clothes():



class ClothesTests(TestCase):
    
    @classmethod 
    def setUpTestData(cls):
        distributor =  models.Distributor.objects.create(distributor_name="John Doe",contact_email="Johndoe@gmail.com")
        brand = models.Brand.objects.create(brand_name="Calvin Klein",distributor=distributor)
        
        type_clothe1 = models.Type_Clothe.objects.create(type_name="Jacket")
        type_clothe2 = models.Type_Clothe.objects.create(type_name="T-Shirt")
        
        color1 = models.Colors.objects.create(color_name="Black",color="#000000")
        color2 = models.Colors.objects.create(color_name="White",color="#FFFFFF")
        
        size1 = models.Sizes.objects.create(size="S")
        size2 = models.Sizes.objects.create(size="M")
        
        clothe_male = models.Clothes.objects.create(
            description="Jacket UX",
            type_clothe=type_clothe1,
            gender="M",
            brand=brand,
            price=29.99,
            units=10,
            
        )      
        image = models.image_for_clothe.objects.create()
        image.image.save('jacket_calvin_test.jpg',File(open("clothes/media_tes/jacket_calvin_test.jpg",'rb')))
        images_and_color1 = models.image_and_color_of_clothe.objects.create()
        images_and_color1.images.add(image)
        images_and_color1.color = color1
        images_and_color1.save()
        
        
        images_and_color2 = models.image_and_color_of_clothe.objects.create()
        images_and_color2.images.add(image)
        images_and_color2.color = color2
        images_and_color2.save()
        
        clothe_male.ColorImages.add(images_and_color1)
        clothe_male.ColorImages.add(images_and_color2)
        # clothe_male.image.save('jacket_calvin_test.jpg',File(open("clothes/media_tes/jacket_calvin_test.jpg",'rb')))
        clothe_male.sizes.set([size1,size2])
        clothe_male.save()
        
        clothe_female = models.Clothes.objects.create(
            description="T-shirt UX",
            type_clothe=type_clothe2,
            gender="F",
            brand=brand,
            price=20.99,
            units=10,
        )
        image = models.image_for_clothe.objects.create()
        image.image.save('calvin_klein_tshirt_test.jpg',File(open("clothes/media_tes/calvin_klein_tshirt_test.jpg",'rb')))
        images_and_color1 = models.image_and_color_of_clothe.objects.create()
        images_and_color1.images.add(image)
        images_and_color1.color=color1 
        images_and_color1.save()
        
        images_and_color2 = models.image_and_color_of_clothe.objects.create()
        images_and_color2.images.add(image)
        images_and_color2.color=color2
        images_and_color2.save()
        #clothe_female.image.save('calvin_klein_tshirt_test.jpg',File(open("clothes/media_tes/calvin_klein_tshirt_test.jpg",'rb')))
        
        clothe_female.ColorImages.add(images_and_color1)
        clothe_female.ColorImages.add(images_and_color2)
        clothe_female.sizes.set([size1,size2])
        clothe_female.save()
        
        # for ColorImage in clothe_female.ColorImages.all():
        #     print('ColorImage_color_id: ',ColorImage.color)
    
        
    def setUp(self) -> None:
        self.client = Client()    
    
    
    def test_show_clothes_view(self):
            
        response = self.client.get("/")
        
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.context['items_for_slide_M'][0][1],"/media/resized/jacket_calvin_test_resized.jpg")
        self.assertEqual(response.context['items_for_slide_F'][0][1],"/media/resized/calvin_klein_tshirt_test_resized.jpg")
    
    
    def test_show_male_products(self):
        
        response = self.client.get("/products/M")
            
        self.assertEqual(response.context['clothes'][0].id,3)
        
        self.assertEqual(response.status_code,200)
    
    
    def test_show_female_products(self):
        response = self.client.get('/products/F')
        
        self.assertEqual(response.context['clothes'][0].id,4)
        self.assertEqual(response.status_code,200)
    
    
    def test_show_detail_products(self):
        
        response = self.client.get("/products/3")
        
        self.assertEqual(response.context['clothe'].id,3)
        self.assertEqual(response.status_code,200)    
    
    
    def test_fail_show_product(self):
        response = self.client.get("/products/5")
        
        self.assertEqual(response.context['clothe'],None)    
    
    
    def test_z_delete_media(self):
                     
        if os.path.isfile("media/resized/jacket_calvin_test_resized.jpg"):     
            os.remove("media/resized/jacket_calvin_test_resized.jpg")        
        
        if os.path.isfile("media/clothes_media/jacket_calvin_test.jpg"):
            os.remove("media/clothes_media/jacket_calvin_test.jpg")
        
        if os.path.isfile("media/resized/calvin_klein_tshirt_test_resized.jpg"):
            os.remove("media/resized/calvin_klein_tshirt_test_resized.jpg")
        
        if os.path.isfile("media/clothes_media/calvin_klein_tshirt_test.jpg"):
            os.remove("media/clothes_media/calvin_klein_tshirt_test.jpg")