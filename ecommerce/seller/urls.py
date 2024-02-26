from django.urls import path
from seller import views

urlpatterns = [
    path('create/', views.SellerViewSet.as_view({'post':'post'}), name='create_seller'),
    path('change/', views.SellerViewSet.as_view({'put':'put','delete':'delete'}), name='change_seller'),
    path('list/', views.SellerViewSet.as_view({'get':'get_list'}), name='get_sellers'),
    path('one/', views.SellerViewSet.as_view({'get':'get'}), name='get_seller'),
]