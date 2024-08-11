from django.urls import path
from . import views

urlpatterns = [
    path('age_modal', views.age_modal, name='age_modal')
]