from django import forms
from datetime import datetime
from contenido.models import TAGS_CHOICES

class CommentaryForm(forms.Form):

    text_commentary = forms.CharField()

class PublicationForm(forms.Form):

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


class NewTagForm(forms.Form):

    tag = forms.CharField(max_length= 4)
    label = forms.CharField(max_length= 50)