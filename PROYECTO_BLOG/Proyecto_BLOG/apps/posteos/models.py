from django.db import models

class Posteo(models.Model):
	titulo = models.CharField(max_length=250) 
	cuerpo = models.CharField()