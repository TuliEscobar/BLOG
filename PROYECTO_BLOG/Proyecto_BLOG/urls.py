
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Inicio.as_view(), name="inicio"),
    #path('', views.inicio, name= "inicio"),  #pagina de inicio
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name= "login"),
    path('logout', auth_views.logout_then_login, name="logout"),
    path("nuevo/", views.NuevoPost.as_view(), name="nuevopost"),
    path("editar/<int:pk>", views.EditarPost.as_view(), name="editarpost"),
    

    #Includes
    path("posteo/", include('apps.posteos.urls'), name="posteo"),
    path("Usuario/", include('apps.usuarios.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
