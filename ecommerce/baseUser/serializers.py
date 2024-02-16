from rest_framework import serializers
from baseUser.models import (
    User
)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
