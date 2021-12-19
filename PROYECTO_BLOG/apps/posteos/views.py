
from django.views.generic import ListView, DetailView

from apps.core.mixins import AdminRequiredMixins
from .models import Posteo

class ListarAdmin(AdminRequiredMixins, ListView):
    template_name= "posteos/admin/listar.html"
    model = Posteo
    context_object_name="posteos"

    def get_queryset(self):
        return Posteo.objects.all().order_by("id")

class Detalle(DetailView):
	template_name = "posteos/detalle.html"
	model = Posteo 


