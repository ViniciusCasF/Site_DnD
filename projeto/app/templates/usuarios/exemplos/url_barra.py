# urls.py
from django.urls import path
from .views import editar_progresso

urlpatterns = [
    path('editar_progresso/', editar_progresso, name='editar_progresso'),
]
