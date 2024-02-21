from rest_framework import serializers
from baseUser.serializers import UserSerializer
from client.models import (
    Client
)
from baseUser.models import User, register_user



class ClientSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(required=False, write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user_values = validated_data.pop('user_data')
        user_values['user_type'] = User.UserType.CLIENT
        client = register_user(**user_values,**validated_data)

        return client

    
    

    