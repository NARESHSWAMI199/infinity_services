from django.contrib import admin
from django.urls import path,include
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls'),name='core'),
    path('accounts/', include('accounts.urls'),name='account'),
    path('usr_profile/',include('profiles.urls'),name='profile'),
]+static (
    settings.MEDIA_URL , document_root = settings.MEDIA_ROOT
)
