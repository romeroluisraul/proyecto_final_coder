from django.urls import path
from contenido.views import *

urlpatterns = [

    path('busqueda/<tag>/', tags, name='tags'),
]