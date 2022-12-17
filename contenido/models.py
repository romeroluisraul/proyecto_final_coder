from django.db import models
from django.utils.timezone import now as django_now
from datetime import date

class Post(models.Model):

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

    tag1 = models.CharField(max_length=4, choices=TAGS_CHOICES)
    tag2 = models.CharField(max_length=4, choices=TAGS_CHOICES)

    title = models.TextField(max_length=50, unique=True)
    subtitle = models.TextField(max_length=80)

    description = models.TextField(max_length=300)
    text_content = models.TextField(max_length=7000, blank=True)
    date = models.DateField(default=django_now)

    image_portada = models.ImageField(upload_to='portadas_post', null=False, blank=False)
    image_contenido = models.ImageField(upload_to='contenido_post', null=True, blank=True)
    image_portada_alt = models.CharField(max_length=50)
    image_portada_title = models.CharField(max_length=50)
    image_contenido_alt = models.CharField(max_length=50, blank=True)
    image_contenido_title = models.CharField(max_length=50, blank=True)

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

        respuesta = self.related_post.title + ': ' + self.commentarist

        return respuesta

def get_comments(ActualPost: Post) -> list:

  comentarios = Commentary.objects.filter(related_post = ActualPost)

  return comentarios

def quantity_comments(ActualPost: Post) -> list:

  comentarios = Commentary.objects.filter(related_post = ActualPost)

  return len(comentarios)

setattr(Post, "related_comments", get_comments)
setattr(Post, "quantity_comments", quantity_comments)

    