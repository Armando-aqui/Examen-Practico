from django.db import models

# Create your models here.

class Tareas(models.Model):
  titulo = models.CharField(max_length=200)
  descripcion = models.TextField(blank=True)
  completada = models.BooleanField(default=False)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  fecha_actualizacion = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return self.titulo
