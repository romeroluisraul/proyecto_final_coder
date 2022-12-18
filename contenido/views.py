from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from contenido.models import *
from contenido.forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from datetime import date
from time import sleep

contexto = {'anio' : str(date.today().year)}

def home(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = request.get_full_path()
    contexto['posteos'] = Post.objects.all()

    return render(request, 'home.html', contexto)

def autor(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = request.get_full_path() 

    return render(request, 'autor.html', contexto)

def tags(request, tag):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = request.get_full_path()

    etiqueta = tag
    posts = Post.objects.filter(Q(tag1__icontains=etiqueta) | Q(tag2__icontains=etiqueta))

    def choices(tag):

        TRAVEL,AR,CL = 'TR','AR','CL'
        CUYO, PATAGONIA, COSTA, BUENOS_AIRES, CENTRO = 'CY','PAT','MDP','BSAS','COB'
        PARQUES, LAGOS, RUTAS, MONTANIAS = 'PN','LG','RN','MNT'
        IDEAS, RATA_TIPS = 'ID','TIP'

        TAGS_CHOICES = [(TRAVEL, 'Travel'),
                        (AR, 'Argentina'), (CL, 'Chile'),
                        (CUYO, 'Cuyo'), (PATAGONIA, 'Patagonia'), (COSTA, 'Costa Atlántica'),
                        (BUENOS_AIRES, 'Buenos Aires'), (CENTRO, 'Centro'),
                        (PARQUES, 'Parques'), (LAGOS, 'Lagos'), (RUTAS, 'Rutas'), (MONTANIAS, 'Montañas'),
                        (IDEAS, 'Ideas'), (RATA_TIPS, 'Rata-tips')]

        i = 0
        while TAGS_CHOICES[i][0] != tag.upper():
            i += 1

        return(TAGS_CHOICES[i][1])

    contexto['tag_buscado'] = choices(etiqueta)
    contexto['posts'] = posts

    return render(request, 'resultados.html', contexto)

def visualizar_publicacion(request, post):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = request.get_full_path()

    posteo = Post.objects.get(title = post)

    contexto['post'] = posteo
    contexto['texto_post'] = posteo.text_content.split(sep = '\n')

    contexto['image_contenido_list'] = [{'url': posteo.image_contenido.url,'title': posteo.image_contenido_title, 'alt': posteo.image_contenido_alt, 'paragraph': posteo.image_contenido_paragraph},
                                        {'url': posteo.image_contenido2.url,'title': posteo.image_contenido2_title, 'alt': posteo.image_contenido2_alt, 'paragraph': posteo.image_contenido2_paragraph},
                                        {'url': posteo.image_contenido3.url,'title': posteo.image_contenido3_title, 'alt': posteo.image_contenido3_alt, 'paragraph': posteo.image_contenido3_paragraph},
                                        {'url': posteo.image_contenido4.url,'title': posteo.image_contenido4_title, 'alt': posteo.image_contenido4_alt, 'paragraph': posteo.image_contenido4_paragraph},
                                        ]

    return render(request, 'contenido_post.html', contexto)

def pagina_comentarios(request, post):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = request.get_full_path()

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
