from django.db import models
from django.utils.timezone import now as django_now
from datetime import date
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.conf import settings

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

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=User.objects.get(username='romeroluisraul').pk, on_delete = models.SET_DEFAULT)

    tag1 = models.CharField(max_length=4, choices=TAGS_CHOICES)
    tag2 = models.CharField(max_length=4, choices=TAGS_CHOICES)

    title = models.TextField(max_length=50, unique=True)
    subtitle = models.TextField(max_length=80)

    description = models.TextField(max_length=300)
    text_content = models.TextField(max_length=7000, blank=True)
    date = models.DateField(default=django_now)

    image_portada = models.ImageField(upload_to='portadas_post')
    image_portada_alt = models.CharField(max_length=50)
    image_portada_title = models.CharField(max_length=50)

    image_contenido = models.ImageField(upload_to='contenido_post', null=True, blank=True)
    image_contenido_alt = models.CharField(max_length=50, blank=True, null=True)
    image_contenido_title = models.CharField(max_length=50, blank=True, null=True)
    image_contenido_paragraph = models.TextField(max_length=500, blank=True, null=True)

    image_contenido2 = models.ImageField(upload_to='contenido_post', null=True, blank=True)
    image_contenido2_alt = models.CharField(max_length=50, blank=True, null=True)
    image_contenido2_title = models.CharField(max_length=50, blank=True, null=True) 
    image_contenido2_paragraph = models.TextField(max_length=500, blank=True, null=True)

    image_contenido3 = models.ImageField(upload_to='contenido_post', null=True, blank=True)
    image_contenido3_alt = models.CharField(max_length=50, blank=True, null=True)
    image_contenido3_title = models.CharField(max_length=50, blank=True, null=True)
    image_contenido3_paragraph = models.TextField(max_length=500, blank=True, null=True)
    
    image_contenido4 = models.ImageField(upload_to='contenido_post', null=True, blank=True)
    image_contenido4_alt = models.CharField(max_length=50, blank=True, null=True)
    image_contenido4_title = models.CharField(max_length=50, blank=True, null=True)  
    image_contenido4_paragraph = models.TextField(max_length=500, blank=True, null=True)      

    @property
    def date_avaliable(self):
        return date.today() >= self.date

    def __str__(self):
        return self.title

class Commentary(models.Model):

    commentarist = models.TextField(max_length=20)
    text_commentary = models.TextField(max_length= 400)
    date_commentary = models.DateTimeField()
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):

        respuesta = self.related_post.title + ': ' + self.commentarist + ' at ' + self.date_commentary.strftime('%d/%m/%Y, %H:%M:%S')

        return respuesta

def get_comments(ActualPost: Post) -> list:

  comentarios = Commentary.objects.filter(related_post = ActualPost)

  return comentarios

setattr(Post, "related_comments", get_comments)


    