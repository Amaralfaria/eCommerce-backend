from django.urls import path
from product import views

urlpatterns = [
    path('create/', views.ProductViewSet.as_view({'post':'post'})),
    path('change/<int:pk>', views.ProductViewSet.as_view({'put':'put','delete':'delete'})),
    path('list/', views.ProductViewSet.as_view({'get':'get_list'})),
    path('list/my_products', views.ProductViewSet.as_view({'get':'get_seller_list'})),
    path('one/<int:pk>', views.ProductViewSet.as_view({'get':'get'})),
]