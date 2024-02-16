from django.contrib import admin
from baseUser import models

admin.site.register(models.User)
admin.site.register(models.UserType)
