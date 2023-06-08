from django.urls import path
from .views import (
  home,
  car_list,
  car_detail,
  customer_list,
  customer_detail,
  reservation_list,
  reservation_detail)


urlpatterns = [
    path('', home),
    path('cars/', car_list),
    path('car_detail/<int:pk>', car_detail),
    path('customers/', customer_list),
    path('customer_detail/<int:pk>', customer_detail),
    path('reservations/', reservation_list),
    path('reservation_detail/<int:pk>', reservation_detail),
    
]