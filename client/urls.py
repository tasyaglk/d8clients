from django.urls import path
from . import views

urlpatterns = [
    path('my_profile', views.client_profile, name="client_profile")
]