from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse

from purchase.models import Purchase
from client.models import Client
from client.views import IsOwnerOrReadOnlyClient
from purchase.serializers import PurchaseSerializer

class PurchaseViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsOwnerOrReadOnlyClient]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def get_list(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)