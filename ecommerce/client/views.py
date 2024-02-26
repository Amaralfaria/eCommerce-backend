from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse

from client.models import Client
from baseUser.views import IsOwnerOrReadOnly
from client.serializers import ClientSerializer

class IsOwnerOrReadOnlyClient(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.client == Client.objects.get(user=request.user)

class ClientViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_object(self):
        return Client.objects.get(user=self.request.user)

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
    
    
    
    
    