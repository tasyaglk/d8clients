from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('', views.main, name="main"),
    path('about', views.about_us, name="about_us")
]


