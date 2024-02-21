from rest_framework import serializers
from product.models import (
    Product
)
from seller.models import Seller
from seller.serializers import CurrentSellerDefault

class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all(),default=CurrentSellerDefault())
    class Meta:
        model = Product
        fields = '__all__'


    