from django.shortcuts import render

from apps.posteos.models import Posteo

#def inicio(request):
	

def inicio(request):
    posteos = Posteo.objects.all()
    context={
        "posteos" : posteos
        }
    return render(request, "inicio.html", context)

