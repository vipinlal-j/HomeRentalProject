
from django.urls import path
from User import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from HouseRentalManagementSystem import settings


urlpatterns = [
    path('index/', views.index, name="index"),
    path('user_register/', views.user_register, name="user_register"),
    path('user_save/', views.user_save, name="user_save"),

    path('add_post/', views.add_post, name="add_post"),
    path('save_post/', views.save_post, name="save_post"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)