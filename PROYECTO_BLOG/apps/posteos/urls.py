
from django.urls import path

from . import views

app_name= "posteos"

urlpatterns = [
    path('', views.detalle, name= "posteo"),
    path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
    
]