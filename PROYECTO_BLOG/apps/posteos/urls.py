from typing import ValuesView
from django.urls import path

from . import views

app_name= "posteo"

urlpatterns = [
    path('', views.detalle, name= "posteo")

]