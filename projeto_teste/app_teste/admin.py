# admin.py

from django.contrib import admin
from .models import Magia  # Importa o modelo que você criou

admin.site.register(Magia)  # Registra o modelo no admin
