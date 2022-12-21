from django.urls import path
from contenido.views import *

urlpatterns = [

    path('busqueda/<tag>/', tags, name='tags'),
    path('visualizar/<post>/', visualizar_publicacion, name = 'visualizar'),
    path('visualizar/<post>/comments', pagina_comentarios, name = 'comentarios'),
    path('crear/nuevo_post/', crear_nuevo_post, name = 'nuevo_post')
]