from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse

from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer

class PurchaseViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)