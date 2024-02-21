from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    seller = models.ForeignKey('seller.Seller', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
