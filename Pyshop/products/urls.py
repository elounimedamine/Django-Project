from django.urls import path #import le path
from . import views #on va allez dans le view

#inclue les urls dans le 2nd fichier
urlpatterns = [ #contient les urls
    path('products', views.index), #importer le path
]

