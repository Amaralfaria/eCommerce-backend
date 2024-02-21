from django.db import models

class Seller(models.Model):
    user = models.ForeignKey('baseUser.User', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.store_name