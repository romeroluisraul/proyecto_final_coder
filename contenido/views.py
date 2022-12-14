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

contexto = {'anio' : str(date.today().year),
                   'title': 'Explorando Parques Nacionales',
                   'title_description': 'La Argentina cuenta con 38 Parques Nacionales únicos en el mundo. ',
                   'fecha': date.today()}

def home(request):

    contexto['home_url'] = request.get_full_path() == '/home/'
    contexto['pagina_actual'] = request.get_full_path()
    contexto['posteos'] = Post.objects.all()

    return render(request, 'home.html', contexto)
