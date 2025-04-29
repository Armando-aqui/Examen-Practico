from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TareaSerializer
from .models import Tareas

# Create your views here.

class TareaVista(viewsets.ModelViewSet):
  serializer_class = TareaSerializer
  queryset = Tareas.objects.all()