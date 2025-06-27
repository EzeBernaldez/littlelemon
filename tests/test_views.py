from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class MenuViewTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        
        self.user = User.objects.create_user(username='eze', password='261073eB')
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        Menu.objects.create(Title='Pizza mediana',Price=2.25,Inventory=2)
        Menu.objects.create(Title='Pizza chica',Price=1.25,Inventory=2)
        Menu.objects.create(Title='Pizza grande',Price=3.25,Inventory=2)
    
    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(response.data, serializer.data)