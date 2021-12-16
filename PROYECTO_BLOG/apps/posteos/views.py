from django.shortcuts import render
from django.views.generic import ListView

from apps.posteos.forms import PosteoForm
from .models import Posteo


def detalle(request):
    context= {}
    return render(request, "posteos/detalle.html", context)

class ListarAdmin(ListView):
    template_name= "posteos/admin/listar.html"
    model = Posteo
    context_object_name="posteos"

    def get_queryset(self):
        return Posteo.objects.all().order_by("id")