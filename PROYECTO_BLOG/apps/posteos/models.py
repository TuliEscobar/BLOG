from django.db import models

from apps.usuarios.models import Usuario

class Categoria(models.Model):
	nombre= models.CharField(max_length=255)
	

class Meta:
	db_table="categorias"
def __str__(self):
	return self.nombre

class Posteo(models.Model):
	titulo = models.CharField(max_length=250) 
	cuerpo = models.TextField()
	categorias = models.ManyToManyField(Categoria)
	imagen = models.ImageField(upload_to="posteos", null=True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True)


class Meta:
	db_table="posteos"
	def __init__(self):
		return self.titulo


