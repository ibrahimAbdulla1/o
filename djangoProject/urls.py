from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('register/', views.registerPage, name='register'),
    path('guest/', views.guestPage, name='guest'),
    path('diagnosis/', views.diagnosis_view, name='diagnosis'),
]



