from rest_framework import serializers
from review.models import (
    Review
)
from client.serializers import CurrentClientDefault
from client.models import Client


class ReviewSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(),default=CurrentClientDefault())
    class Meta:
        model = Review
        fields = '__all__'

    