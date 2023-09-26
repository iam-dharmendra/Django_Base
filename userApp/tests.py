from django.test import TestCase
from .models import User
from .serializer import RegisterSerializer
from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.


class test_user_model(TestCase):

# test model
    def test_user(self):
        email="abc@example.com"
        password="abc123"

        
        user=User.objects.create_user(email=email,password=password)
        self.assertEqual(email,user.email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

# test serializer
    def test_serializer(self):

        data={'password':'253','password2':'253'}
        serializer=RegisterSerializer(data=data)

        # self.assertFalse(serializer.is_valid())
        # self.assertEqual(serializer.errors,{'non_field_errors':["both passeord must same"]})

        self.assertTrue(serializer.is_valid())



class Blog_test_api(APITestCase):


    def test_blog_all(self):
        # self.factory = RequestFactory()
        # request = self.factory.get("/customer/details")

        response=self.client.get(reverse('blog_post_list'))
        # response=self.client.post(reverse(),data={'name':a})
        # response=self.client.put(reverse(),data={'name':a})
        print(response.context)
        self.assertEqual(response.status_code,200)


""" to find which part of code are not test and which part of code test use coverage module (pip install coverage check docs) basically

it genrate report of your test cases. docs:https://docs.djangoproject.com/en/4.2/topics/testing/advanced/"""        