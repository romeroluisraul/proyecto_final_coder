from django.shortcuts import render, redirect
from contenido.models import *
from contenido.forms import *
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from autenticacion.views import *

from datetime import date
from time import sleep
from contenido.models import TAGS_CHOICES

def choices(tag):

    i = 0
    while TAGS_CHOICES[i][0].upper() != tag.upper():
        i += 1
    return TAGS_CHOICES[i][1]

def choices_inverse(label):
    i = 0
    while TAGS_CHOICES[i][1].upper() != label.upper():
        i += 1
    return TAGS_CHOICES[i][0]

contexto = {'anio' : str(date.today().year)}
contexto['tags'] = TAGS_CHOICES.copy()

def home(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())
    contexto['posteos'] = Post.objects.all().order_by("date")

    contexto['tags_usados'] = set([post.tag1 for post in Post.objects.all()])
    contexto['tags_usados'] = list(contexto['tags_usados'].union(set([ post.tag2 for post in Post.objects.all()])))

    return render(request, 'home.html', contexto)

def autor(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())

    return render(request, 'autor.html', contexto)

def redirect_home(request):

    return redirect('home')

def tags(request, tag):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['ultima_pagina'] = str(request.get_full_path())

    etiqueta = tag
    posts = Post.objects.filter(Q(tag1__icontains=etiqueta) | Q(tag2__icontains=etiqueta)).order_by("-date")

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
def notificacion_actualizacion(request):

    if contexto['contador'] == 0:

        contexto['contador'] += 1
        contexto['tags_usados'] = set([ post.tag1 for post in Post.objects.all()])
        contexto['tags_usados'] = list(contexto['tags_usados'].union(set([ post.tag2 for post in Post.objects.all()])))
        
        respuesta = render(request, 'guardar_post.html', contexto)

    else:
        sleep(2)
        respuesta = redirect('home')

    return respuesta

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
            contexto['contador'] = 0
            respuesta = redirect('confirmacion_cambios')

        else:

            errors = mi_formulario.errors 
            contexto['errors'] = errors
            respuesta = render(request, 'crear_nuevo_post.html', contexto)
            
    if request.method == 'GET':
        
        contexto['script'] = False
        respuesta = render(request, 'crear_nuevo_post.html', contexto)

    return respuesta

@user_passes_test(lambda user: user.is_superuser)
def editar_post(request, post):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['choices'] = TAGS_CHOICES

    Posteo = Post.objects.get(title = post)
    contexto['title'] = post

    default_values = {'tag1':  Posteo.tag1, 'tag2':  Posteo.tag2,
                    'tag1_label': choices(Posteo.tag1), 'tag2_label': choices(Posteo.tag2),
                    'title':  Posteo.title, 'subtitle':  Posteo.subtitle,
                    'description':  Posteo.description, 'text_content':  Posteo.text_content,
                    'date':  Posteo.date,
                    'image_portada':  Posteo.image_portada, 'image_portada_alt':  Posteo.image_portada_alt, 'image_portada_title':  Posteo.image_portada_title}

    contexto['default_values'] = default_values

    if request.method == 'POST':

        mi_formulario = PublicationForm(request.POST, files = request.FILES)
        
        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data    

            atributos = ['tag1','tag2','title','subtitle','description','text_content','date']
            atributos += ['image_portada','image_portada_alt','image_portada_title']

            for atributo in atributos:

                setattr(Posteo, atributo, informacion[atributo])

            Posteo.save()

            contexto['script'] = True
            contexto['contador'] = 0

            respuesta = redirect('confirmacion_cambios')

        else:

            errors = mi_formulario.errors 
            contexto['errors'] = errors

            respuesta = render(request, 'editar_post.html', contexto)
            
    if request.method == 'GET':

        contexto.pop('errors', None)
        contexto['script'] = False

        respuesta = render(request, 'editar_post.html', contexto)

    return respuesta

@user_passes_test(lambda user: user.is_superuser)
def editar_galeria(request, post):

    contexto['home_url'] = request.get_full_path() == '/home/'

    Posteo = Post.objects.get(title = post)

    if request.method == 'POST':

        mi_formulario = ImageGalleryForm(request.POST, files = request.FILES)
        
        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data   

            atributos = ['image_contenido','image_contenido_alt','image_contenido_title','image_contenido_paragraph']
            atributos += ['image_contenido2','image_contenido2_alt','image_contenido2_title','image_contenido2_paragraph']
            atributos += ['image_contenido3','image_contenido3_alt','image_contenido3_title','image_contenido3_paragraph']
            atributos += ['image_contenido4','image_contenido4_alt','image_contenido4_title','image_contenido4_paragraph']

            i = 0
            while atributos[i] in informacion.keys():
                
                setattr(Posteo, atributos[i], informacion[atributos[i]]) 
                i += 1

            Posteo.save()
            contexto['script'] = True

        else:

            errors = mi_formulario.errors 
            contexto['errors'] = errors
            
    if request.method == 'GET':

        contexto.pop('errors', None)

        imagen_1 = {'name': 'Imagen 1',
                    'image_name_on_form': 'image_contenido',
                    'image_alt_on_form': 'image_contenido_alt',
                    'image_alt_value': Posteo.image_contenido_alt,
                    'image_title_on_form': 'image_contenido_title',
                    'image_title_value': Posteo.image_contenido_title,
                    'images_paragraph_on_form': 'image_contenido_paragraph',
                    'image_paragraph_on_form': Posteo.image_contenido_paragraph,
                    }

        imagen_2 = {'name': 'Imagen 2',
                    'image_name_on_form': 'image_contenido2',
                    'image_alt_on_form': 'image_contenido2_alt',
                    'image_alt_value': Posteo.image_contenido2_alt,
                    'image_title_on_form': 'image_contenido2_title',
                    'image_title_value': Posteo.image_contenido2_title,
                    'images_paragraph_on_form': 'image_contenido2_paragraph',
                    'image_paragraph_on_form': Posteo.image_contenido2_paragraph,
                    }

        imagen_3 = {'name': 'Imagen 3',
                    'image_name_on_form': 'image_contenido3',
                    'image_alt_on_form': 'image_contenido3_alt',
                    'image_alt_value': Posteo.image_contenido3_alt,
                    'image_title_on_form': 'image_contenido3_title',
                    'image_title_value': Posteo.image_contenido3_title,
                    'images_paragraph_on_form': 'image_contenido3_paragraph',
                    'image_paragraph_on_form': Posteo.image_contenido3_paragraph,
                    }

        contexto['imagenes'] = [imagen_1,imagen_2,imagen_3]

    return render(request, 'editar_galeria.html', contexto)

@user_passes_test(lambda user: user.is_superuser)
def eliminar_post(request, post):

    contexto['home_url'] = request.get_full_path() == '/home/'

    Posteo = Post.objects.get(title = post)
    Posteo.delete()

    return redirect('home')

@user_passes_test(lambda user: user.is_superuser)
def agregar_tag(request):

    contexto['home_url'] = request.get_full_path() == '/home/'

    if request.method == 'POST':

        mi_formulario = NewTagForm(request.POST)

        tags_usados = set([post.tag1 for post in Post.objects.all()] + [ post.tag2 for post in Post.objects.all()])
        etiquetas_usadas = set([choices(tag) for tag in tags_usados])

        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data

            if informacion['label'].capitalize() not in etiquetas_usadas and informacion['tag'].upper() not in tags_usados: 

                TAGS_CHOICES.append((informacion['tag'].upper(), informacion['label'].capitalize()))

                contexto['tags'] = TAGS_CHOICES.copy()

                contexto['tags_usados'] = set([ post.tag1 for post in Post.objects.all()])
                contexto['tags_usados'] = list(contexto['tags_usados'].union(set([ post.tag2 for post in Post.objects.all()])))

                contexto['script'] = True

                respuesta = redirect('nuevo_tag')

            else:

                contexto['errors'] = 'El tag o la etiqueta de tag que pretende agregar ya se encuentra definida.'

                respuesta = render(request, 'agregar_tags.html', contexto)

        else:
            errors = mi_formulario.errors 
            contexto['errors'] = errors

            respuesta = render(request, 'agregar_tags.html', contexto)

    if request.method == 'GET':

        contexto.pop('errors', None)
        contexto['script'] = False

        respuesta = render(request, 'agregar_tags.html', contexto)

    return respuesta


