from rest_framework import serializers
from baseUser.serializers import UserSerializer
from client.models import (
    Client, register_client
)
from baseUser.models import User



class ClientSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(required=False, write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):
        user_values = validated_data.pop('user_data')
        client = register_client(name=validated_data['name'],password=user_values['password'],email=user_values['email'])

        return client

    
    

    