from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from ..custom_client import Custom_Client

# Create your tests here.


class UserTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("jose","joselopez@gmail.com","1234")
        
    
    def setUp(self):
        self.customClient = Custom_Client()
        
        
    def test_login(self):
            
        response = self.client.post("/user/login",data={"email_user":"joselopez@gmail.com","password_user":"1234"})
        
        self.assertEqual(response.url,"/")
        self.assertEqual(response.status_code,302)
        
    
    def test_info(self):
        self.customClient.login(username="jose",password="1234")
        
        response = self.customClient.get("/user/info")
        
        self.assertEqual(response.context['username'],'jose')
        
    
    def test_logout(self):
        
        self.customClient.login_by_email(email="joselopez@gmail.com",password="1234")
        
        response = self.customClient.get("/user/logout")
        
        self.assertEqual(response.url,"/user/login")
        self.assertEqual(response.status_code,302)
        
    def test_sigup(self):
        
        response = self.customClient.post('/user/sigup',data={"username":"Julian",
                                                   "email_user":"josejulianpower@gmail.com",
                                                   "password_user_1":"password1234",
                                                   "password_user_2":"password1234"})
        
        self.assertEqual(response.url,"/")
        
    
    def test_change_password(self):
        self.customClient.login_by_email(email="joselopez@gmail.com",password="1234")
        
        response = self.customClient.post("/user/change-password",data={"old_password":"1234",
                                                                        "password_1":"new_password",
                                                                        "password_2":"new_password"})
        
        self.assertEqual(response.url,"/")
        
    
    def test_change_email(self):
        
        self.customClient.login_by_email(email="joselopez@gmail.com",password="1234")
        
        response = self.customClient.post("/user/change-email",data={"password_user":"1234",
                                                                     "new_email":"josejulianpower@gmail.com"})
        
        self.assertEqual(response.url,"/user/info")
        
        