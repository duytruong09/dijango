from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('order/', views.Order.as_view(), name='order'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('menu/search/', views.MenuSearch.as_view(), name='menu-search'),
    path('order-confirmation/<int:pk>', views.OrderConfirmation.as_view(), name='order-confirmation'),
    path('payment-confirmation/', views.OrderPayConfirmation.as_view(), name='payment-confirmation'),
]