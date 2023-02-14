import requests
from django.test import TestCase
from django.conf import settings


class CocksTestCase(TestCase):
    """
        CockTail Api TestCase
        
    """
    
    def setUp(self) -> None:
        self.api_url = settings.API_URL
    
    
    def test_search_drink(self):
        name = 'margarita'
        response = requests.get(self.api_url + name, timeout=10)
        list_drinks = response.json()
        self.assertEqual(list_drinks['drinks'][0]['strDrink'], 'margarita')
