from django.test import TestCase 
from restaurant.models import Menu

class MenuTest(TestCase):
    
    def test_instance(self):
        item = Menu.objects.create(Title='LomoPizza', Price=12.00, Inventory=10)
        self.assertEqual(str(item), 'LomoPizza : 12.0')