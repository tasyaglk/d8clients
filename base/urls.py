from django.urls import path, include
from . import views

urlpatterns = [
    path('clients/', include('client.urls')),
    path('business/', include('staff.urls')),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('', views.main, name="main"),
    path('about', views.about_us, name="about_us"),
    path('registration/', views.registration_page, name="registration")
]


