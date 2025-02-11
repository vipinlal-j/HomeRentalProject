from django.contrib import admin
from django.urls import path
from User import views
from Client import views

urlpatterns = [
    path('client_index/', views.client_index, name="client_index"),
    path('register_client/', views.register_client, name="register_client"),
    path('save_client/', views.save_client, name="save_client"),

    path('client_home/', views.client_home, name="client_home"),
    path('ClientLogin/', views.ClientLogin, name="ClientLogin"),
    path('ClientLoginAuth/', views.ClientLoginAuth, name="ClientLoginAuth"),


]