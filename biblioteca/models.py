from django.db import models

# Create your models here.

class Autor(models.Model):
  nombre = models.CharField(max_length=100)
  fecha_nacimiento = models.DateField()

  def __str__(self) -> str:
    return self.nombre
  

class Libro(models.Model):
  titulo = models.CharField(max_length=200)
  autor = models.CharField(max_length=100)
  fecha_publicacion = models.DateField()

  def __str__(self) -> str:
    return self.titulo
