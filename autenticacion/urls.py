from django.urls import path
from autenticacion.views import *

urlpatterns = [

    path("login/", logeo_user, name = 'log_in'),
    path("logout/", deslogeo_user, name = 'log_out'),
    path("logout/<destino>", deslogeo_user, name = 'log_out_param'),
    path('user/bienvenido/', bienvenida, name = 'bienvenida'),
]