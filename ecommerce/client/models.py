from django.db import DatabaseError, models
from django.db import transaction
from baseUser.models import register_user, User

class Client(models.Model):
    user = models.ForeignKey('baseUser.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

def register_client(name,  email, password):
    try:
        with transaction.atomic():
            user = register_user(email=email,password=password,user_type=User.UserType.CLIENT)
            client = Client.objects.create(user=user,name=name)
    except DatabaseError as DBe:
        raise

    return client




