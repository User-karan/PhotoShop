from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('membership_success/', views.membership_success, name='membership_success'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
]

