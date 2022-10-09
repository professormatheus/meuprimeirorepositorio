from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('Sobre/', views.sobre, name='sobre'),
    path('Contato/', views.contato, name='contato'),
]