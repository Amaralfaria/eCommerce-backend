from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from seller.models import Seller
from seller.serializers import SellerSerializer

class SellerViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        