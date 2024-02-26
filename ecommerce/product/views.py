from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer

class ProductViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    
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
