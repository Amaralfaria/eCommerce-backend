from django.urls import path
from review import views

urlpatterns = [
    path('create/', views.ReviewViewSet.as_view({'post':'post'}), name='create_review'),
    path('change/<int:pk>', views.ReviewViewSet.as_view({'put':'put','delete':'delete'})),
    path('list/', views.ReviewViewSet.as_view({'get':'get_list'})),
    path('one/<int:pk>', views.ReviewViewSet.as_view({'get':'get'})),
]