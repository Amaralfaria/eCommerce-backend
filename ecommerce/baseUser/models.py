from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserType(models.Model):
    description = models.CharField(max_length=15)

    def __str__(self):
        return self.description


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
        extra_fields.setdefault("user_type",UserType.objects.get(description="superuser"))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    user_type = models.ForeignKey(UserType,on_delete=models.DO_NOTHING)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def is_staff(self):
       return True

    def has_perm(self, perm, obj=None):
       return self.user_type == UserType.objects.get(description="superuser")

    def has_module_perms(self, app_label):
       return self.user_type == UserType.objects.get(description="superuser")


    def __str__(self):
        return self.email





