from django.urls import path, include

from . import views

urlpatterns = [
    path('magic-link/', views.magic_link, name='magic_link'),
 ]