from django.urls import path
from baseUser import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('create/', views.UsuarioViewSet.as_view({'post':'create_user'}), name='create_usuario'),
    path('login/', TokenObtainPairView.as_view(), name='get_token'),
    path('test_auth/', views.AutheticationViewSet.as_view({'post':'test_auth'}), name='test token'),
]