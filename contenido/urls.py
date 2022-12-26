from django.urls import path
from contenido.views import *

urlpatterns = [

    path('busqueda/<tag>/', tags, name='tags'),
    path('visualizar/<post>/', visualizar_publicacion, name = 'visualizar'),
    path('visualizar/<post>/comments', pagina_comentarios, name = 'comentarios'),
    path('crear/nuevo_post/', crear_nuevo_post, name = 'nuevo_post'),
    path('editar/<post>', editar_post, name = 'editar_post'),
    path('editar/<post>/galeria', editar_galeria, name = 'editar_galeria'),
    path('eliminar/<post>/', eliminar_post, name = 'eliminar_post'),
    path('confirmacion/', notificacion_actualizacion, name = 'confirmacion_cambios'),
]