from django.urls import path
from purchase import views

urlpatterns = [
    path('create/', views.PurchaseViewSet.as_view({'post':'post'}), name='create_purchase'),
]