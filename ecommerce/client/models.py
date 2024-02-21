from django.db import models

class Client(models.Model):
    user = models.ForeignKey('baseUser.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



