from django.urls import path
from . import views

urlpatterns = [
    path('services', views.services, name='services'),
    path('services_prices', views.services_prices, name='services_prices'),
    path('walks', views.walks, name='walks'),
]
