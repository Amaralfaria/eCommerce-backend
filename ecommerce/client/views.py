from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from django.http import JsonResponse

from client.models import Client
from client.serializers import ClientSerializer

class ClientViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)