from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    client = models.ForeignKey('client.Client', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    comment = models.TextField(max_length=300)
    date_time = models.DateTimeField(auto_now_add=True)
