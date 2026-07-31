from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='football-home'),
    path('about/', views.about, name='football-about'),
]