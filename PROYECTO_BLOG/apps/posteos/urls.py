
from django.urls import path

from . import views

app_name= "posteos"

urlpatterns = [
    path("Admin/Listar/", views.ListarAdmin.as_view(), name="admin_listar"),
    path("Detalle/<int:pk>", views.Detalle.as_view(), name = "detalle")
]