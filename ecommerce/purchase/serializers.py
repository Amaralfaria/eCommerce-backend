from rest_framework import serializers
from client.models import Client
from purchase.models import (
    Purchase
)
from client.serializers import CurrentClientDefault

class PurchaseSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(),default=CurrentClientDefault())
    class Meta:
        model = Purchase
        fields = '__all__'

    