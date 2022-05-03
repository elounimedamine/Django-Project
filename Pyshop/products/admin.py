from django.contrib import admin
from .models import Product #improrter les produits du models.py

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock') #afficher la liste des infos qui s'affiche dans le site

admin.site.register(Product, ProductAdmin) #pour enregistrer ces informations de Product de la form ProductAdmin
