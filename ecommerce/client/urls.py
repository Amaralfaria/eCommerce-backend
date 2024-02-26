from django.urls import path
from client import views

urlpatterns = [
    path('create/', views.ClientViewSet.as_view({'post':'post'}), name='create_client'),
    path('change/', views.ClientViewSet.as_view({'put':'put','delete':'delete'}), name='change_client'),
    path('list/', views.ClientViewSet.as_view({'get':'get_list'}), name='get_clients'),
    path('one/', views.ClientViewSet.as_view({'get':'get'}), name='get_client'),
]