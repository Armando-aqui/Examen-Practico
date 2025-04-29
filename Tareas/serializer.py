from rest_framework import serializers
from .models import Tareas

class TareaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tareas
    #field = ('id', 'titulo', 'descripcion', 'completado', 'fecha_creacion', 'fecha_actualizacion')
    fields = '__all__'