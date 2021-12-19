from django import forms
from . models import Posteo

class PosteoForm(forms.ModelForm):
    titulo= forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
 
    class Meta:
        model = Posteo
        fields = ["titulo", "cuerpo", "imagen","categorias"]

