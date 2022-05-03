from django.shortcuts import render
from django.http import HttpResponse #just pour le test

# Create your views here.
from .models import Product #importer les models from Product

def index(request):
   product = Product.objects.all() #importer tous les objets(produits) de product
   return render(request, 'index.html', {'produits' : product}) #rendre le résultat de index.html et les produits

