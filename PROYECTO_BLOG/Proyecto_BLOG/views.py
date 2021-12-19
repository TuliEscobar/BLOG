from django.shortcuts           import render
from django.views.generic  import TemplateView, ListView, CreateView
from django.urls                import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.posteos.models        import Posteo
from apps.posteos.forms         import PosteoForm
from django.views.generic.edit  import UpdateView

class Inicio(TemplateView):
    template_name= "inicio.html"

    def get_context_data(self,**kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context ["posteos"] = Posteo.objects.all()
        return context


class NuevoPost(LoginRequiredMixin, CreateView):
    template_name = "posteos/nuevo.html"
    model = Posteo
    form_class = PosteoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("inicio")
        
    def form_valid(self,form):
        f = form.save(commit=False)
        f.usuario_id = self.request.user.id
        return super(NuevoPost, self).form_valid(form)



class EditarPost(LoginRequiredMixin, UpdateView):
    template_name = "posteos/editar.html"
    model = Posteo
    form_class = PosteoForm

    def get_success_url(self, **kwargs):
        return reverse_lazy("inicio")

