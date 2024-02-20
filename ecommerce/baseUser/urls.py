from django.urls import path
from baseUser import views

urlpatterns = [
    path('create/', views.UsuarioViewSet.as_view({'post':'create_user'}), name='create_usuario'),
    path('login/', views.AutheticationViewSet.as_view({'post':'login'}), name='get_token'),
    path('test_auth/', views.AutheticationViewSet.as_view({'post':'test_auth'}), name='test token'),
]