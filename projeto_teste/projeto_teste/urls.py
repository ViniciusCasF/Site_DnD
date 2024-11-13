from app_teste import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('entrar/', views.entrar, name='entrar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('personagem_tipo/', views.personagem_tipo, name='personagem_tipo'),
    path('escolher_origem/<int:personagem_id>/', views.escolher_origem, name='escolher_origem'), 
    path('escolher_habilidades/<int:personagem_id>/', views.escolher_habilidades,name='escolher_habilidades'),
    path('calcular_vida/<int:personagem_id>/', views.calcular_vida, name='calcular_vida'),
    path('escolher_pericias/<int:personagem_id>/', views.escolher_pericias, name='escolher_pericias'),
    path('escolher_antecedentes/<int:personagem_id>/', views.escolher_antecedentes, name='escolher_antecedentes'),
    path('escolher_caracteristicas/<int:personagem_id>/', views.escolher_caracteristicas, name='escolher_caracteristicas'),
    path('pagina_teste/<int:personagem_id>/', views.pagina_teste, name='pagina_teste'),
    path('ficha/<int:personagem_id>/', views.ficha, name='ficha'),
    path('manMagias/<int:personagem_id>/', views.manMagias, name='manMagias'),
    path('inventario/<int:personagem_id>/', views.inventario, name='inventario'),
]
