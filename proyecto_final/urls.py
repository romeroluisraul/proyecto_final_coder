"""proyecto_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

### importar las vistas de las aplicaiones
import autenticacion.views as autenticacion
import contenido.views as contenido

### para las imagenes de los modelos
from proyecto_final.settings import MEDIA_ROOT, MEDIA_URL
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', contenido.home, name = 'home'),
    path('posts/', include("contenido.urls")),
]

urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)