# Examen Técnico - API de Tareas (Django)

Este proyecto es parte del Examen Técnico para Desarrollador Junior. Consiste en una API REST creada con Django y Django REST Framework para gestionar tareas.

---

## Requisitos

- Python 3.10+
- pip
- Git
- Virtualenv

---

## Instrucciones para ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Armando-aqui/Examen-Practico.git
cd Examen-Practico
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv env
source env/bin/activate                # En Windows: env\Scripts\activate
pip install -r requirements.txt      #Instalar dependencias
```

### 3. Aplicar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Ejecutar el Servidor

```bash
python manage.py runserver
```

### 5. La API estara disponible en
http://127.0.0.1:8000/Tareas/api/v1/Tareas/


---
## Parte 2 - Ejercicios prácticos
- Modelos Django de biblioteca (libro y autor) están en `biblioteca/models.py`.
- Funciones de Python en `ejercicios_practicos.py`:
  - Ordenar una lista.
  - Contar palabras de un archivo (`texto.txt`).
- Script MySQL en `ejercicios_mysql.sql`.

Para probar el script de Python, ejecutar:
```bash
python ejercicios_practicos.py
```
