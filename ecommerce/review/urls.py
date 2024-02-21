from django.urls import path
from review import views

urlpatterns = [
    path('create/', views.ReviewViewSet.as_view({'post':'post'}), name='create_review'),
]