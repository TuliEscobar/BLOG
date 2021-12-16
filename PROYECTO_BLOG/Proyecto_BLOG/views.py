from django.shortcuts           import render
from django.views.generic.base  import TemplateView
from django.views.generic       import CreateView
from django.urls                import reverse_lazy

from apps.posteos.models        import Posteo
from apps.posteos.forms         import PosteoForm
from django.views.generic.edit  import UpdateView

class Inicio(TemplateView):
    template_name= "inicio.html"

    def get_context_data(self,**kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context ["posteos"] = Posteo.objects.all()
        return context


class NuevoPost(CreateView):
    template_name = "posteos/nuevo.html"
    model = Posteo
    form_class = PosteoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("inicio")
        

class EditarPost(UpdateView):
    template_name = "posteos/editar.html"
    model = Posteo
    form_class = PosteoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("inicio")