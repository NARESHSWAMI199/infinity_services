
from django.urls import path
from .views import (
    login_view,registor_view,logout_view
)
app_name = 'accounts'
urlpatterns = [ 
    path ('signup/',registor_view,name='signup'),
    path ('login/',login_view,name='login'),
    path ('logout/',logout_view,name='logout')
]