
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
path('', views.index,name="home")  ,  
path("about", views.about,name="about")  ,  
path("contact", views.contact,name="about")  ,  
path("services", views.services,name="services")  ,path('index', views.index,name="home")  , 
    path('login', views.loginuser,name="login"),
path('logout', views.logoutuser,name="logout"),
]