from django.shortcuts import render, redirect
from contenido.models import *
from contenido.forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.files.storage import FileSystemStorage
from autenticacion.views import *

from datetime import date
from time import sleep

TAGS_CHOICES = [('TR', 'Travel'),
                ('AR', 'Argentina'), ('CL', 'Chile'),
                ('CY', 'Cuyo'), ('PAT', 'Patagonia'), ('MDP', 'Costa Atlántica'),
                ('BSAS', 'Buenos Aires'), ('COB', 'Centro'),
                ('PN', 'Parques'), ('LG', 'Lagos'), ('RN', 'Rutas'), ('MNT', 'Montañas'),
                ('ID', 'Ideas'), ('TIP', 'Rata-tips')]

contexto = {'anio' : str(date.today().year)}

def choices(tag):

    i = 0
    while TAGS_CHOICES[i][0] != tag.upper():
        i += 1
    return(TAGS_CHOICES[i][1])

contexto['posteos'] = Post.objects.all()
contexto['tags'] = TAGS_CHOICES.copy()
contexto['tags_usados'] = set([ post.tag1 for post in contexto['posteos']])
contexto['tags_usados'] = list(contexto['tags_usados'].union(set([ post.tag2 for post in contexto['posteos']])))

def home(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())
    contexto['posteos'] = Post.objects.all()

    return render(request, 'home.html', contexto)

def autor(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())

    return render(request, 'autor.html', contexto)

def tags(request, tag):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())

    etiqueta = tag
    posts = Post.objects.filter(Q(tag1__icontains=etiqueta) | Q(tag2__icontains=etiqueta))

    contexto['tag_buscado'] = choices(etiqueta)
    contexto['posts'] = posts

    return render(request, 'resultados.html', contexto)

def visualizar_publicacion(request, post):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())

    posteo = Post.objects.get(title = post)

    contexto['post'] = posteo
    contexto['texto_post'] = posteo.text_content.split(sep = '\n')

    try:

        contexto['image_contenido_list'] = [{'url': posteo.image_contenido.url,'title': posteo.image_contenido_title, 'alt': posteo.image_contenido_alt, 'paragraph': posteo.image_contenido_paragraph},
                                        {'url': posteo.image_contenido2.url,'title': posteo.image_contenido2_title, 'alt': posteo.image_contenido2_alt, 'paragraph': posteo.image_contenido2_paragraph},
                                        {'url': posteo.image_contenido3.url,'title': posteo.image_contenido3_title, 'alt': posteo.image_contenido3_alt, 'paragraph': posteo.image_contenido3_paragraph},
                                        {'url': posteo.image_contenido4.url,'title': posteo.image_contenido4_title, 'alt': posteo.image_contenido4_alt, 'paragraph': posteo.image_contenido4_paragraph},
                                        ]

    except ValueError:
        
        contexto['image_contenido_list'] = []

    return render(request, 'contenido_post.html', contexto)

def pagina_comentarios(request, post):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())

    posteo = Post.objects.get(title = post)

    if request.method == 'POST':

        mi_formulario = CommentaryForm(request.POST)
        
        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            nuevo_comentario = Commentary(commentarist = request.user,
                                    text_commentary = informacion['text_commentary'],
                                    date_commentary = datetime.now(),
                                    related_post = posteo)
            nuevo_comentario.save()
            contexto['script'] = True

        else:

            errors = mi_formulario.errors 
            contexto['errors'] = errors
            
    mi_formulario = CommentaryForm()

    contexto['post'] = posteo
    contexto['comments'] = posteo.related_comments()
    contexto['form'] = mi_formulario

    contexto['script'] = False

    return render(request, 'comentarios.html', contexto)


@user_passes_test(lambda user: user.is_superuser)
def crear_nuevo_post(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['choices'] = TAGS_CHOICES

    if request.method == 'POST':

        mi_formulario = PublicationForm(request.POST, files = request.FILES)
        
        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data    

            nuevo_post = Post(tag1 = informacion['tag1'], tag2 = informacion['tag2'],
                              title = informacion['title'], subtitle = informacion['subtitle'],
                              description = informacion['description'], text_content = informacion['text_content'],
                              date = informacion['date'],
                              image_portada = informacion['image_portada'], image_portada_alt = informacion['image_portada_alt'], image_portada_title = informacion['image_portada_title'])

            nuevo_post.save()
            contexto['script'] = True

        else:

            errors = mi_formulario.errors 
            contexto['errors'] = errors
            
    if request.method == 'GET':

        contexto['script'] = False

    return render(request, 'crear_nuevo_post.html', contexto)