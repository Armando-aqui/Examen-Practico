from django.urls import path, include
from rest_framework import routers
from Tareas import views

router = routers.DefaultRouter()
router.register(r'Tareas', views.TareaVista, 'Tareas')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
