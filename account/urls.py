from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *


urlpatterns = [
    # path('send_otp/', send_otp),
    path('send_sms/', send_sms_to_login),
    path('login/', login_user),
    path('logout/', logout_user),
    path('register/', register_user),
    # path('register/', register),
]
