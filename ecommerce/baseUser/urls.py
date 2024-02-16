from django.urls import path
from baseUser import views

urlpatterns = [
    path('create/', views.UsuarioViewSet.as_view({'post':'create_user'}), name='create_usuario'),
]