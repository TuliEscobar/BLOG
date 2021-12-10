
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),  #pagina de inicio
    path('login/', views.login)
]
