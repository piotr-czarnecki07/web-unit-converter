from django.urls import path
from Unit_Converter import views

urlpatterns = [
    path('', views.main, name='main'),
    path('length/', views.length, name='length'),
    path('mass/', views.mass, name='mass'),
    path('temperature/', views.temperature, name='temperature'),
]