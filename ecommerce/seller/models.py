from django.db import DatabaseError, models
from django.db import transaction
from baseUser.models import register_user, User

class Seller(models.Model):
    user = models.ForeignKey('baseUser.User', on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.store_name
    

def register_seller(store_name, email, password):
    try:
        with transaction.atomic():
            user = register_user(email=email,password=password,user_type=User.UserType.SELLER)
            seller = Seller.objects.create(user=user,store_name=store_name)
    except DatabaseError as DBe:
        raise

    return seller
