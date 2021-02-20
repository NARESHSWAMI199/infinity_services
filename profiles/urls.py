from django.contrib import admin
from django.urls import path,include
from .views import (user_profile,client_dashboard,edit_dash)

app_name ='profiles'


urlpatterns = [
    path('',user_profile,name='user_profile'),
    path('dashboard/',client_dashboard,name='dashboard'),
    path('eidt/',edit_dash,name='edit')
]


