from django.shortcuts import render


def detalle(request):
    context= {
        
    }
    return render(request, "posteos/detalle.html", context)