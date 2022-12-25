from django import forms
from datetime import datetime

class CommentaryForm(forms.Form):

    text_commentary = forms.CharField()

class PublicationForm(forms.Form):

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

    tag1 = forms.ChoiceField(choices=TAGS_CHOICES)
    tag2 = forms.ChoiceField(choices=TAGS_CHOICES)
    
    title = forms.CharField(max_length=50)
    subtitle = forms.CharField(max_length=80)

    description = forms.CharField(max_length=300)
    text_content = forms.CharField(max_length=7000)
    date = forms.DateField()

    image_portada = forms.ImageField()
    image_portada_alt = forms.CharField(max_length=50)
    image_portada_title = forms.CharField(max_length=50)

class ImageGalleryForm(forms.Form):

    image_contenido = forms.ImageField(required=False)
    image_contenido_alt = forms.CharField(max_length=50, required=False)
    image_contenido_title = forms.CharField(max_length=50, required=False)
    image_contenido_paragraph = forms.CharField(max_length=500, required=False)

    image_contenido2 = forms.ImageField(required=False)
    image_contenido2_alt = forms.CharField(max_length=50, required=False)
    image_contenido2_title = forms.CharField(max_length=50, required=False) 
    image_contenido2_paragraph = forms.CharField(max_length=500, required=False)

    image_contenido3 = forms.ImageField(required=False)
    image_contenido3_alt = forms.CharField(max_length=50, required=False)
    image_contenido3_title = forms.CharField(max_length=50, required=False)
    image_contenido3_paragraph = forms.CharField(max_length=500, required=False)
    
    image_contenido4 = forms.ImageField(required=False)
    image_contenido4_alt = forms.CharField(max_length=50, required=False)
    image_contenido4_title = forms.CharField(max_length=50, required=False)  
    image_contenido4_paragraph = forms.CharField(max_length=500, required=False)