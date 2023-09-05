from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from ..custom_client import Custom_Client

# Create your tests here.


class UserTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user("jose","usertest@gmail.com","1234")
        
    
    def setUp(self):
        self.customClient = Custom_Client()
        
        
    def test_login(self):
            
        response = self.client.post("/user/login",data={"email_user":"usertest@gmail.com","password_user":"1234"})
        
        self.assertEqual(response.url,"/")
        self.assertEqual(response.status_code,302)
        
    
    def test_info(self):
        self.customClient.login(username="jose",password="1234")
        
        response = self.customClient.get("/user/info")
        
        self.assertEqual(response.context['username'],'jose')
        
    
    def test_logout(self):
        
        self.customClient.login_by_email(email="usertest@gmail.com",password="1234")
        
        response = self.customClient.get("/user/logout")
        
        self.assertEqual(response.url,"/user/login")
        self.assertEqual(response.status_code,302)
        
    def test_sigup(self):
        
        response = self.customClient.post('/user/sigup',data={"username":"Julian",
                                                   "email_user":"usertest2@gmail.com",
                                                   "password_user_1":"password1234",
                                                   "password_user_2":"password1234"})
        
        self.assertEqual(response.url,"/")
        
    
    def test_change_password(self):
        self.customClient.login_by_email(email="usertest@gmail.com",password="1234")
        
        response = self.customClient.post("/user/change-password",data={"old_password":"1234",
                                                                        "password_1":"new_password",
                                                                        "password_2":"new_password"})
        
        self.assertEqual(response.url,"/")
        
    
    def test_change_email(self):
        
        self.customClient.login_by_email(email="usertest@gmail.com",password="1234")
        
        response = self.customClient.post("/user/change-email",data={"password_user":"1234",
                                                                     "new_email":"usertest3@gmail.com"})
        
        self.assertEqual(response.url,"/user/info")
        
    
    def test_fail_login(self):
        
        response = self.customClient.post("/user/login",data={"email_user":"usertest@gmail.com",
                                                   "password_user":"12345"})
        
        self.assertEqual(response.context['error'],"Password or email invalid")
        
        response = self.customClient.post("/user/login",data={"email_user":"usertest.com",
                                                              "password_user":"password1234"})
        
        self.assertEqual(response.context['error'],"write a valid email")
        
    
    def test_fail_sigup(self):
        
        response = self.customClient.post("/user/sigup",data={"username":"Julian",
                                                              "email_user":"usertest3@gmail.com.com",
                                                              "password_user_1":"password1",
                                                              "password_user_2":"password2"})
        
        self.assertEqual(response.context['error'],"Passwords are not equals")
        
        response = self.customClient.post("/user/sigup",data={"username":"Julian",
                                                              "email_user":"usertest3@gmail",
                                                              "password_user_1":"password1",
                                                              "password_user_2":"password2"})
        
        self.assertEqual(response.context['error'],"Invalid Email")
    
    
    def test_fail_change_password(self):
        self.customClient.login_by_email(email="usertest@gmail.com",password="1234")
        
        response = self.customClient.post("/user/change-password",data={"old_password":"1234",
                                                                        "password_1":"pass123",
                                                                        "password_2":"pass1234"})
        
        self.assertEqual(response.context['error'],"Passwords are not equals")
        
        response = self.customClient.post("/user/change-password",data={"old_password":"123",
                                                                        "password_1":"pass1234",
                                                                        "password_2":"pass1234"})
        
        self.assertEqual(response.context['error'],"Password incorrect")
        
    
    
    def test_fail_change_email(self):
        User.objects.create_user("julian","usertest3@gmail.com","1234")
        
        self.customClient.login_by_email(email="usertest3@gmail.com",password="1234")
        
        response = self.customClient.post("/user/change-email",data={"password_user":"1234",
                                                                     "new_email":"usertest4.com"})
        
        self.assertEqual(response.context['error'],"Incorrect email")
        
        response2 = self.customClient.post("/user/change-email",data={"password_user":"12345",
                                                                     "new_email":"usertest4@gmail.com"})
        
        self.assertEqual(response2.context['error'],"Password incorrect")
        
        