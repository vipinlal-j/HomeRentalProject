from django.contrib import admin
from django.urls import path
from Admin import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('view_users/', views.view_users, name="view_users"),
    path('delete_user/<int:cat_id>/', views.delete_user, name="delete_user"),

    path('AdminLogin/', views.AdminLogin, name="AdminLogin"),
    path('AdminLoginAuth/', views.AdminLoginAuth, name="AdminLoginAuth"),
    path('AdminLogout/', views.AdminLogout, name="AdminLogout"),
    path('AddCategory/', views.AddCategory, name="AddCategory"),
    path('SaveCategory/', views.SaveCategory, name="SaveCategory"),
    path('DisplayCategory/', views.display_categories, name="DisplayCategory"),
    path('editCat/<int:cat_id>/', views.editCat, name="editCat"),
    path('updateCat/<int:cat_id>/', views.updateCat, name="updateCat"),
    path('deleteCat/<int:cat_id>/', views.deleteCat, name="deleteCat"),

    path('view_client/', views.view_client, name="view_client"),
    path('delete_client/<int:cat_id>/', views.delete_client, name="delete_client"),

]