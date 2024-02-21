from django.urls import path
from product import views

urlpatterns = [
    path('create/', views.ProductViewSet.as_view({'post':'post'}), name='create_product'),
]