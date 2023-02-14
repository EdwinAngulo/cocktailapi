from django.http import JsonResponse
from rest_framework.views import APIView
from cockapi.cocktail_api import CocktailApi
import csv

# Create your views here.

class SearchView(APIView):
    """
        Search Api View
    """
    
    def get(self, request):
        name = request.GET.get('name', '')
        return self.search(name)

    def search(self, name):
        list_cocktails = CocktailApi().search(name=name)
        return JsonResponse(list_cocktails)


