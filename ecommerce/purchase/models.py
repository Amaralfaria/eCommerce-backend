from django.db import models

class Purchase(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField('product.Product')

