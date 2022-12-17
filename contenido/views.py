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
    contexto['script'] = False

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
