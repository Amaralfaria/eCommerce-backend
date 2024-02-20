from rest_framework import mixins, viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse

from baseUser.models import User
from baseUser.serializers import UserSerializer


class UsuarioViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def create_user(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AutheticationViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = User
    permission_classes = [permissions.AllowAny]
    
    def login(self,request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.get(email=email)

        if user is None:
            return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)
        
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)

            return JsonResponse(
                {
                    "refresh": str(refresh),
                    "access_token": str(refresh.access_token)
                }
            )
        else:
            return Response('Wrong password', status=status.HTTP_401_UNAUTHORIZED)
        
    def test_auth(self,request):
        user = request.user
        print(user)
        return Response(status=status.HTTP_200_OK)

    


    

    
