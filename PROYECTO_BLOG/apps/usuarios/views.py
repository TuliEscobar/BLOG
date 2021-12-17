from django.shortcuts import render

from django.views.generic  import ListView, CreateView
from django.urls                import reverse_lazy

from .models import Usuario
from .forms import UsuarioForm

class Registrarme(CreateView):
    template_name = "usuarios/registrar.html"
    model = Usuario
    form_class = UsuarioForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("inicio")