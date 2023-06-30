from django.urls import path
from core import views

urlpatterns = [

    path('index/', views.indexView, name='index'),

    path('publicaciones/', views.publicacionesView, name ='publicaciones'),
]