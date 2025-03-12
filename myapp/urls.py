from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('pay/',views.lipa_na_mpesa_online,name='pay')]