from django.db import models


class Categoria(models.Model):
	nombre= models.CharField(max_length=255)

class Meta:
	db_table="categorias"
	def __str__(self):
		return self.nombre

class Posteo(models.Model):
	titulo = models.CharField(max_length=250) 
	cuerpo = models.CharField(max_length=9999)
	categorias = models.ManyToManyField(Categoria)


class Meta:
	db_table="posteos"
	def __init__(self):
		return self.titulo


