from rest_framework import serializers
from baseUser.models import (
    User
)



class UserSerializer(serializers.ModelSerializer):
    user_type = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = '__all__'

    
