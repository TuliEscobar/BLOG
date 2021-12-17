from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import Usuario


class UsuarioForm(UserCreationForm):   
    username = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={"class": "form-control"}))
    dni = forms.CharField(label="Dni", widget=forms.TextInput(attrs={"class": "form-control"}))
    
    password1 = forms.CharField(label="Contraseña", widget=forms.TextInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirme Contraseña", widget=forms.TextInput(attrs={"class": "form-control"}))

    
    class Meta:
        model = Usuario
        fields = ["username", "first_name", "last_name", "email", "dni"]
