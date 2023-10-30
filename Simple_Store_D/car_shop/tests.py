from django.test import TestCase
from clothes import models 
from django.contrib.auth.models import User
from django.test import Client
from django.core.files import File
import os

# Create your tests here.


class ShoppingCartTests(TestCase):
    
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
        
        clothe_female.sizes.set([size1,size2])
        clothe_female.save()
        User.objects.create_user(username='Julian',email="shoppingcarttest@gmail.com",password='password1234')    
        
        
    def setUp(self) -> None:
        self.client = Client()
        
        self.client.login(username="Julian",password="password1234")
    
    
    def test_add_to_car(self):
        
        string_id = '1-1-1'
        
        response = self.client.get("/car-shop/add/"+string_id)
        
        self.assertEqual(response.json()['clothe_id'],str(1))
        
        
    def test_add_to_car_twice(self):
        
        string_id = '1-1-2'
        string_id2 = '1-1-2'
        
        response = self.client.get("/car-shop/add/"+string_id)
        
        self.assertEqual(response.json()['clothe_id'],str(1))
        
        response = self.client.get("/car-shop/add/"+string_id2)
        
        self.assertEqual(response.json()['units'],2)
        
        
    def test_add_and_low_car(self):
        
        string_id = '1-1-1'
        
        response = self.client.get('/car-shop/add/'+string_id)
        
        self.assertEqual(response.json()['units'],1)
        
        response = self.client.get("/car-shop/add/"+string_id)
        
        self.assertEqual(response.json()['units'],2)
        
        response = self.client.get('/car-shop/low/'+string_id)
        
        self.assertEqual(response.json()['units'],1)
        
    
    def test_del_clothe_shopping_cart(self):
        
        string_id = '1-1-1'
        
        response = self.client.get("/car-shop/add/"+string_id)
        
        self.assertEqual(response.json()['units'],1)
        
        response = self.client.get("/car-shop/del/"+string_id)
        
        self.assertEqual(response.json()['clothe_id'],'1')
        
        
    def test_clear_clothe_shopping_cart(self):
        
        response = self.client.get('/car-shop/clear')
        
        self.assertEqual(response.json()['response'],"V")
        

    def test_create_order(self):
        string_id = '1-1-1'
        
        response = self.client.get("/car-shop/add/"+string_id)
        
        self.assertEqual(response.json()['clothe_id'],'1')
        
        response = self.client.get("/car-shop/order")
        
        self.assertEqual(response.json()['response'],"V")


    def test_z_delete_media(self):
                
        if os.path.isfile("media/resized/jacket_calvin_test_resized.jpg"):     
            os.remove("media/resized/jacket_calvin_test_resized.jpg")        
        
        if os.path.isfile("media/clothes_media/jacket_calvin_test.jpg"):
            os.remove("media/clothes_media/jacket_calvin_test.jpg")
        
        if os.path.isfile("media/resized/calvin_klein_tshirt_test_resized.jpg"):
            os.remove("media/resized/calvin_klein_tshirt_test_resized.jpg")
        
        if os.path.isfile("media/clothes_media/calvin_klein_tshirt_test.jpg"):
            os.remove("media/clothes_media/calvin_klein_tshirt_test.jpg")