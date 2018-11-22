from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^menu/nuevo/$', views.menu_nuevo, name='menu_nuevo'),
    path('menu/<int:pk>/', views.post_detail, name='post_detail'),
    ]