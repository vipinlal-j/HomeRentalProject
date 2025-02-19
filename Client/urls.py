from django.contrib import admin
from django.urls import path
from User import views
from Client import views

urlpatterns = [
    path('client_index/', views.client_index, name="client_index"),
    path('register_client/', views.register_client, name="register_client"),
    path('save_client/', views.save_client, name="save_client"),

    path('client_home/', views.client_home, name="client_home"),
    # path('filtered/<cat_name>/', views.filtered, name="filtered"),

    path('ClientLogin/', views.ClientLogin, name="ClientLogin"),
    path('ClientLoginAuth/', views.ClientLoginAuth, name="ClientLoginAuth"),
    path('SingleProduct/<int:pro_id>/', views.SingleProduct, name="SingleProduct"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('booking/<int:pro_id>/', views.booking, name="booking"),
    path('cart/', views.cart, name="cart"),
    path('cartview/', views.cartview, name="cartview"),
    path('logout/', views.ClientLogout, name='ClientLogout'),
    # path('payment/', views.payment, name="payment"),

    #payment
    path('payment/<int:booking_id>/', views.payment, name='payment'),
    path('payment-success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('paymenthistory/', views.paymenthistory, name="paymenthistory"),

    #ratings and reviews
    path('review/<int:pro_id>/', views.review, name="review"),
    path('save_review/', views.save_review, name="save_review"),

    path('cartDelete/<int:crt_id>/', views.cartDelete, name="cartDelete"),
    path('save_payment/<str:booking_id>/', views.save_payment_details, name='save_payment'),

]