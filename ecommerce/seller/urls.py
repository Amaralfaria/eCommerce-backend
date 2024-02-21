from django.urls import path
from seller import views

urlpatterns = [
    path('create/', views.SellerViewSet.as_view({'post':'post'}), name='create_seller')
]