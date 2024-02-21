from rest_framework import serializers
from seller.models import (
    Seller
)
from baseUser.models import User, register_user
from baseUser.serializers import UserSerializer

class CurrentSellerDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return Seller.objects.get(user=serializer_field.context['request'].user)

class SellerSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(required=False)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Seller
        fields = '__all__'

    def create(self,validated_data):
        user_values = validated_data.pop('user_data')
        user_values['user_type'] = User.UserType.SELLER
        seller = register_user(**user_values,**validated_data)

        return seller


    

    