"""
    Cocktail api module
"""
import requests
from django.conf import settings


class Drink:
    """
        Drink data object
    """

    def __init__(self, id_drink, name):
        self.id_drink = id_drink
        self.name = name


class CocktailApi:
    """
        Cocktail api
    """
    api_url = settings.API_URL
    search_url = "search.php?s="


    def search(self, name: str):
        """
            Search drinks
        """
        url = self.api_url + self.search_url + name
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return []
    