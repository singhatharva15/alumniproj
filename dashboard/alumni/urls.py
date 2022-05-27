from django.contrib import admin
from django.urls import path, include
from alumni import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.login),
    path('home/', views.index, name='home'),
    path('career/<username>', views.career, name ='career'),
    # path('career/', views.career),
    path('events', views.events, name='events'),
    path('opportunity', views.opportunity, name='opportunities'), 
    path('updateprofile/<username>', views.updateprofile),
    path('deletebatch/<username>/<int:id>', views.destroyBatch),  
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
