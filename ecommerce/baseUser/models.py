from django.db import DatabaseError, models, transaction

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext as _

from client.models import Client
from seller.models import Seller


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extrafields):
        if not email:
            raise ValueError(("The Email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extrafields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("user_type",User.UserType.SUPERUSER)

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    class UserType(models.IntegerChoices):
        SUPERUSER = 1, _('Superuser'),
        CLIENT = 2, _('Client'),
        SELLER = 3, _('Seller')
        


    email = models.EmailField(unique=True)
    user_type = models.IntegerField(choices=UserType.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_staff(self):
       return True

    def has_perm(self, perm, obj=None):
       return self.user_type == self.UserType.SUPERUSER

    def has_module_perms(self, app_label):
       return self.user_type == self.UserType.SUPERUSER


    def __str__(self):
        return self.email
    

def register_user(email, password, user_type, **kwargs):
    try:
        with transaction.atomic():
            user = User.objects.create_user(email=email,password=password,user_type=user_type)
            sub_user = None
            if user_type == User.UserType.CLIENT:
                sub_user = Client.objects.create(user=user,**kwargs)
            else:
                sub_user = Seller.objects.create(user=user,**kwargs)
    except DatabaseError as DBe:
        raise

    return sub_user
    





