from django import forms
from datetime import datetime

class CommentaryForm(forms.Form):

    text_commentary = forms.CharField()