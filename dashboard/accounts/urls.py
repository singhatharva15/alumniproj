from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('magic-link/', views.magic_link, name='magic_link'),
 ]