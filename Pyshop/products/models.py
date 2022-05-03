from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.name #le nom de produit doit etre affichée à droite