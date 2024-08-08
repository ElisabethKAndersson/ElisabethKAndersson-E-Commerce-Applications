from django.urls import path
from . import views

urlpatterns = [
    path('services_presentation', views.services_presentation, name='services_presentation'),
    path('services_prices', views.services_prices, name='services_prices'),
    path('walks', views.walks, name='walks'),
]
