
from django.urls import path
from User import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from HouseRentalManagementSystem import settings


urlpatterns = [
    path('UserIndex/', views.UserIndex, name="UserIndex"),
    path('RegisterUser/', views.RegisterUser, name="RegisterUser"),
    path('user_save/', views.user_save, name="user_save"),

    path('add_post/', views.add_post, name="add_post"),
    path('save_post/', views.save_post, name="save_post"),
    path('UserLogin/', views.UserLogin, name="UserLogin"),
    path('UserLoginAuth/', views.UserLoginAuth, name="UserLoginAuth"),
    path('UserLogout/', views.UserLogout, name='UserLogout'),

    path('ViewBookings/', views.ViewBookings, name='ViewBookings'),
    path('PostDelete/<int:crt_id>/', views.PostDelete, name="PostDelete"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)