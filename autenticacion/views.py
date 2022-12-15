from django.shortcuts import render
from django.shortcuts import render, redirect
from contenido.models import *
from contenido.forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from contenido.views import contexto

from datetime import date
from time import sleep

def logeo_user(request):

    contexto['home_url'] = request.get_full_path() == '/home/'

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            print(type(form.cleaned_data))

            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password']

            user = authenticate(username=usuario, password = contra)

            if user is not None:

                login(request, user)
                contexto['contador'] = 0
                respuesta = redirect('bienvenida')

            else:
                errores = form.errors
                contexto['errores_acceso'] = errores
                respuesta = render(request, 'acceso_usuarios.html', contexto)
                print(errores)
        else:
            errores = form.errors
            contexto['errores_acceso'] = errores
            respuesta = render(request, 'acceso_usuarios.html', contexto)

    if request.method == 'GET':

        contexto['errores_acceso'] = False
        contexto['form_usuarios'] = True
        respuesta = render(request, 'acceso_usuarios.html', contexto)
    
    form = AuthenticationForm()

    return respuesta

@login_required
def bienvenida(request):

    if contexto['contador'] == 0:

        contexto['contador'] += 1
        respuesta = render(request, 'bienvenida.html', contexto)

    else:
        sleep(2)
        respuesta = redirect(contexto['ultima_pagina'])

    return respuesta

@login_required
def deslogeo_user(request, destino = ''):
    
    logout(request)

    if destino != '':

        respuesta = redirect(destino)

    else:
        sleep(1)
        respuesta = redirect(contexto['ultima_pagina'])

    return respuesta
