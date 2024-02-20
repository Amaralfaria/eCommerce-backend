from django.urls import path
from client import views

urlpatterns = [
    path('create/', views.ClientViewSet.as_view({'post':'post'}), name='create_client'),
]