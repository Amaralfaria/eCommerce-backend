from django.urls import path
from purchase import views

urlpatterns = [
    path('create/', views.PurchaseViewSet.as_view({'post':'post'}), name='create_purchase'),
    path('change/<int:pk>', views.PurchaseViewSet.as_view({'put':'put','delete':'delete'})),
    path('list/', views.PurchaseViewSet.as_view({'get':'get_list'})),
    path('one/<int:pk>', views.PurchaseViewSet.as_view({'get':'get'})),
]