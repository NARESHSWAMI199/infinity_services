from django.contrib import admin
from django.urls import path,include
from .views import (home,
    detail_view,
    client_detail,
)

urlpatterns = [
    path('',home,name='name'),
    path('detail/<int:id>',detail_view,name='detail'),
    path('user_detail/',client_detail,name='user_detail')
]


