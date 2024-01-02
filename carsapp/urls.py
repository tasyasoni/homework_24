from django.urls import path

from carsapp.apps import CarsappConfig
from rest_framework.routers import DefaultRouter

from carsapp.views import CarViewSet, MotoCreateAPIView, MotoListAPIView, MotoRetrieveAPIView, MotoUpdateAPIView, \
    MotoDestroyAPIView

app_name = CarsappConfig.name

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('moto/create/', MotoCreateAPIView.as_view(), name='moto_create'),
    path('moto/list/', MotoListAPIView.as_view(), name='moto_list'),
    path('moto/<int:pk>/', MotoRetrieveAPIView.as_view(), name='moto_one'),
    path('moto/update/<int:pk>/', MotoUpdateAPIView.as_view(), name='moto_update'),
    path('moto/delete/<int:pk>/', MotoDestroyAPIView.as_view(), name='moto_delete'),
] + router.urls