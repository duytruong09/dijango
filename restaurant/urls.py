from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('orders/<int:pk>', views.OrderDetails.as_view(), name='order-details')
]