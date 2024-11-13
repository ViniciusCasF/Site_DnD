from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import Http404
from django.http import JsonResponse
import random

#from .utils import "funcoes"

from django.http import HttpResponse

import json
from .models import Usuario
from .models import Magia
from .models import Personagem
from .models import Habilidades
from .models import Pericias

def home(request):
    return render(request,  'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)

def entrar(request):
    if request.method == 'POST':
        nome_personagem = request.POST.get('texto_nome')
        try:
            personagem = get_object_or_404(Personagem, nome=nome_personagem)
            print(personagem.id_personagem)  # ou o que você quiser fazer com o personagem encontrado
            print(personagem.classes)
            return redirect('ficha', personagem_id=personagem.id_personagem)
        except Http404:
            messages.error(request, 'Personagem não encontrado. Tente novamente.')  # Adiciona mensagem de erro
            return redirect('entrar')  # Redireciona para a página de entrada


    return render(request, 'entrar.html')

def ficha(request, personagem_id):
    return render(request, "ficha.html")

def manMagias(request, personagem_id):
    return render(request, "manMagias.html")

def inventario(request, personagem_id):
    return render(request, "inventario.html")

def cadastrar(request):
    return render(request, 'usuarios/cadastrar.html')

def magias(request):
    nova_magia = Magia()
    nova_magia.nome = request.POST.get('nome')
    nova_magia.nivel = request.POST.get('nivel')
    nova_magia.descricao = request.POST.get('descricao')
    nova_magia.save()

def personagem_tipo(request):
    if request.method == 'POST':
        personagem_id = request.POST.get('personagem_id')
        novo_personagem = Personagem()
        novo_personagem.nome = 'Novo Personagem'
        novo_personagem.descricao = ' '
        novo_personagem.nivel = 1
        novo_personagem.experiencia = 0
        novo_personagem.raca = ' '

        novo_personagem.save()

        nova_habilidade = Habilidades(personagem=novo_personagem)
        nova_habilidade.save()

        nova_pericia = Pericias(personagem=novo_personagem)
        nova_pericia.save()

        classe_selecionada = request.POST.get('bot_escolha')

        novo_personagem.classes = {
            'classe_1': classe_selecionada,
        }

        classes_magia = ['Mago',  'Bardo', 'Bruxo', 'Clérigo', 'Druida', 'Feiticeiro', 'Paladino', 'Patrulheiro']

        if classe_selecionada in classes_magia:
            novo_personagem.pontos_magia = {
                'pontos_magias_1': 2,
            }
        elif classe_selecionada == 'Bárbaro':
            novo_personagem.pontos_magia = {
                'furia': 2
            }
        elif classe_selecionada == 'Monge':
            novo_personagem.pontos_magia = {
                'qi': 2
            }
        #-----------------------------------------------------------Decidindo o dado de vida-----------------------------------------------------------#
        novo_personagem.dado_vida = 0
        #----------------------------------------------------------------------------------------------------------------------------------------------#
        novo_personagem.pontos_magia_atual = novo_personagem.pontos_magia
        novo_personagem.bonus_proeficiencia = 2

        novo_personagem.save()

        return redirect('escolher_origem', personagem_id = novo_personagem.id_personagem)

    return render(request, 'personagem_tipo.html')

def escolher_origem(request, personagem_id):
    personagem = get_object_or_404(Personagem, id_personagem=personagem_id)

    if request.method == 'POST':
        raca = request.POST.get('bot_escolha')
        personagem.raca = raca

        texto = request.POST.get('texto_usuario')
        print(texto)

        personagem.save()
        return redirect('escolher_habilidades', personagem_id)

    context = {
        'personagem': personagem,
        'personagem_id': personagem_id,
    }
    return render(request, 'escolher_origem.html', context)

def escolher_habilidades(request, personagem_id):
    personagem = get_object_or_404(Personagem, id_personagem = personagem_id)
    habilidades = get_object_or_404(Habilidades, personagem = personagem)

    if request.method == 'POST':
        progress_value = {
            'progress_value_1': int(request.POST.get('progress_value_1')),
            'progress_value_2': int(request.POST.get('progress_value_2')),
            'progress_value_3': int(request.POST.get('progress_value_3')),
            'progress_value_4': int(request.POST.get('progress_value_4')),
            'progress_value_5': int(request.POST.get('progress_value_5')),
            'progress_value_6': int(request.POST.get('progress_value_6')),
        }

        habilidades.forca=0
        habilidades.destreza=0
        habilidades.constituicao=0
        habilidades.inteligencia=0
        habilidades.sabedoria=0
        habilidades.carisma=0

        if personagem.raca == 'Anão':
            habilidades.constituicao = 2
        elif personagem.raca == 'Anão da Colina':
            habilidades.sabedoria = 1
        elif personagem.raca == 'Anão da Montanha':
            habilidades.forca = 2
        elif personagem.raca == 'Elfo':
            habilidades.destreza = 2
        elif personagem.raca == 'Elfo da Floresta':
            habilidades.sabedoria = 1
        elif personagem.raca == 'Alto Elfo':
            habilidades.inteligencia = 1
        elif personagem.raca == 'Elfo Negro (Drow)':
            habilidades.carisma = 1
        elif personagem.raca == 'Halfling':
            habilidades.destreza = 2
        elif personagem.raca == 'Pés Leves':
            habilidades.carisma = 1
        elif personagem.raca == 'Robusto':
            habilidades.constituicao = 1
        elif personagem.raca == 'Humano':
            habilidades.forca = 1
            habilidades.destreza = 1
            habilidades.constituicao = 1
            habilidades.inteligencia = 1
            habilidades.sabedoria = 1
            habilidades.carisma = 1
        elif personagem.raca == 'Draconato':
            habilidades.forca = 2
            habilidades.carisma = 1
        elif personagem.raca == 'Gnomo':
            habilidades.inteligencia = 2
        elif personagem.raca == 'Gnomo da Floresta':
            habilidades.destreza = 1
        elif personagem.raca == 'Gnomo das Rochas':
            habilidades.constituicao = 1
        elif personagem.raca == 'Meio Elfo':
            habilidades.carisma = 2
            habilidades.inteligencia = 1
        elif personagem.raca == 'Meio Orc':
            habilidades.forca = 2
            habilidades.constituicao = 1
        elif personagem.raca == 'Thiefling':
            habilidades.inteligencia = 1
            habilidades.carisma = 2

        habilidades.forca = habilidades.forca + progress_value['progress_value_1']
        habilidades.destreza = habilidades.destreza + progress_value['progress_value_2']
        habilidades.constituicao = habilidades.constituicao + progress_value['progress_value_3']
        habilidades.inteligencia = habilidades.inteligencia + progress_value['progress_value_4']
        habilidades.sabedoria = habilidades.sabedoria + progress_value['progress_value_5']
        habilidades.carisma = habilidades.carisma + progress_value['progress_value_6']

        personagem.save()
        habilidades.save()

        return redirect('calcular_vida', personagem_id = personagem.id_personagem)

    context = {
        'personagem': personagem,
        'initial_value_1': 8,
        'initial_value_2': 8,
        'initial_value_3': 8,
        'initial_value_4': 8,
        'initial_value_5': 8,
        'initial_value_6': 8,
        'total_pontos': 27
    }

    return render(request, 'escolher_habilidades.html', context)

def pagina_teste(request, personagem_id):
    return render(request, 'pagina_teste.html')

def calcular_vida(request, personagem_id):
    personagem = get_object_or_404(Personagem, id_personagem = personagem_id)
    habilidades = get_object_or_404(Habilidades, personagem=personagem)


    dado_6 = ['Feiticeiro', 'Mago']
    dado_8 = ['Bardo', 'Bruxo', 'Clerigo', 'Druida', 'Ladino', 'Monge']
    dado_10 = ['Guerreiro', 'Paladino', 'Patrulheiro']

    busca_classe = f'classe_{personagem.nivel}'

    classe = personagem.classes[busca_classe]

    if classe in dado_6:
        personagem.dado_vida = 6
    elif classe in dado_8:
        personagem.dado_vida = 8
    elif classe in dado_10:
        personagem.dado_vida = 10
    elif classe == 'Bárbaro':
        personagem.dado_vida = 12


    if request.method == 'POST':
        data = json.loads(request.body)
        escolha = data.get('escolha')

        if escolha == 'salvar':

            return redirect('escolher_antecedentes', personagem_id=personagem.id_personagem)

        valor_dado = 0

        if escolha == 'metade':
            valor_dado = personagem.dado_vida/2
        elif escolha == 'girar':
            valor_dado = random.randint(1, personagem.dado_vida)

        personagem.vida_maxima = valor_dado + (int)((habilidades.constituicao-10)/2)
        personagem.vida_atual = personagem.vida_maxima
        personagem.save()

        return JsonResponse({'valor_dado': valor_dado, 'personagem_vida': personagem.vida_maxima})
    #teste

    calculo_constituicao = 0
    if habilidades.constituicao<10:
        calculo_constituicao = 0
    else:
        calculo_constituicao = (habilidades.constituicao-10)//2

    context = {
                'dado_vida': 'd'+str(personagem.dado_vida),
                'personagem': personagem,
                'constituicao': calculo_constituicao,
    }

    return render(request, 'escolher_vida.html', context)

def escolher_pericias(request, personagem_id):

    personagem = get_object_or_404(Personagem, id_personagem=personagem_id)
    personagem_pericias = get_object_or_404(Pericias, personagem=personagem)

    busca_classe = f'classe_{personagem.nivel}'
    classe = personagem.classes[busca_classe]

    pericias = []
    quantidade_treinar = 0

    if request.method == 'POST':

        pericias_escolhidas = request.POST.get('pericias_escolhidas', '[]')

        try:
            pericias = json.loads(pericias_escolhidas)  # Decodifica a string JSON
            # Processe as perícias selecionadas
        except json.JSONDecodeError:
            # Retorne uma mensagem de erro amigável ao usuário
            return HttpResponse("Erro ao processar as perícias selecionadas.")

        # Atualize as perícias do personagem no banco de dados
        for pericia in pericias:  # Use 'pericias' aqui
            # Dependendo de como está o seu modelo de Pericias, você pode atualizar assim:
            nome_pericia_banco = pericia.replace(" ", "_")
            setattr(personagem_pericias, nome_pericia_banco, 1)  # Marca como treinado (1)


        personagem_pericias.save()  # Salva as alterações no banco de dados

        return redirect('escolher_caracteristicas', personagem_id=personagem.id_personagem)

        # Redireciona ou envia uma resposta JSON, dependendo da sua necessidade



    if classe == 'Bárbaro':
        pericias = ["Atletismo", "Intimidação", "Lidar com Animais", "Natureza", "Percepção", "Sobrevivência"]
        quantidade_treinar = 2

    elif classe == 'Bardo':
        pericias = ["Acrobacia", "Atletismo", "Atuação", "Arcanismo", "Enganação", "Furtividade", "História", "Intimidação", "Intuição", "Investigação", "Manusear Animais", "Medicina", "Natureza", "Percepção", "Persuasão", "Prestidigitacao", "Religião",
                    "Sobrevivência"]
        quantidade_treinar = 3

    elif classe == 'Bruxo':
        pericias = ["Arcanismo", "Enganação", "História", "Intimidação", "Investigação", "Natureza", "Religião"]
        quantidade_treinar = 2

    elif classe == 'Clerigo':
        pericias = ["História", "Intuição", "Medicina", "Persuasão", "Religião"]
        quantidade_treinar = 2

    elif classe == 'druida':
        pericias = ["Arcanismo", "Intuição", "Manusear Animais", "Medicina", "Natureza", "Percepção", "Religião", "Sobrevivência"]
        quantidade_treinar = 2

    elif classe == 'feiticeiro':
        pericias = ["Arcanismo", "Enganação", "Intimidação", "Intuição", "Persuasão", "Religião"]
        quantidade_treinar = 2

    elif classe == 'guerreiro':
        pericias = ["Acrobacia", "Atletismo", "Historia", "Intimidação", "Intuição", "Manusear Animais", "Percepção", "Sobrevivência"]
        quantidade_treinar = 2

    elif classe == 'ladino':
        pericias = ["Acrobacia", "Atletismo", "Atuação", "Enganação", "Furtividade", "Intimidação", "Intuição", "Investigacao", "Percepção", "Persuasão", "Prestidigitação"]
        quantidade_treinar = 4 #olhar isso aqui

    elif classe == 'mago':
        pericias = ["Arcanismo", "Historia", "Intuição", "Investigacao", "Medicina", "Religião"]
        quantidade_treinar = 2

    elif classe == 'monge':
        pericias = ["Acrobacia", "Atletismo", "Furtividade", "Historia", "Intuição", "Religião"]
        quantidade_treinar = 2

    elif classe == 'paladino':
        pericias = ["Atletismo", "Intimidação", "Intuição", "Medicina", "Persuasão", "Religião"]
        quantidade_treinar = 2

    elif classe == 'patrulheiro':
        pericias = ["Atletismo", "Furtividade", "Intuição", "Investigacao", "Manusear Animais", "Natureza", "Percepção", "Sobrevivência"]
        quantidade_treinar = 3



    if personagem.raca == 'Humano':
        quantidade_treinar = quantidade_treinar+1


# Supondo que o objeto personagem_pericias tenha atributos como atletismo, furtividade, etc.
    pericias_remover = []  # Lista temporária para armazenar as perícias a serem removidas
    for pericia in pericias:
        # Substitui os espaços por underscores para corresponder ao nome no banco de dados
        nome_pericia_banco = pericia.replace(" ", "_") # Trata o nome para acessar corretamente o banco
        # Usa getattr para acessar dinamicamente o valor da perícia no banco
        if getattr(personagem_pericias, nome_pericia_banco, 0) > 0:
            # Se a perícia estiver treinada, adiciona à lista de remoção
            pericias_remover.append(pericia)

    # Agora removemos todas as perícias treinadas de uma vez
    for pericia in pericias_remover:
        pericias.remove(pericia)

    context = {
        'pericias': pericias,
        'quantidade_treinar': quantidade_treinar,
        'personagem': personagem,
    }

    return render(request, 'escolher_pericias.html', context)

def escolher_antecedentes(request, personagem_id):

    personagem = get_object_or_404(Personagem, id_personagem=personagem_id)
    personagem_pericias = get_object_or_404(Pericias, personagem=personagem)

    if request.method == 'POST':

        antecedentes = request.POST.get('bot_escolha')

        if antecedentes == 'Acólito':
            personagem_pericias.Intuição = 2
            personagem_pericias.Religião = 2
        elif antecedentes == 'Artesão de Guilda':
            personagem_pericias.Persuasão = 2
            personagem_pericias.Intuição = 2
        elif antecedentes == 'Artista':
            personagem_pericias.Acrobacia = 2
            personagem_pericias.Atuação = 2
        elif antecedentes == 'Charlatão':
            personagem_pericias.Enganação = 2
            personagem_pericias.Prestidigitação = 2
        elif antecedentes == 'Criança de rua':
            personagem_pericias.Furtividade = 2
            personagem_pericias.Prestidigitação = 2
        elif antecedentes == 'Criminoso':
            personagem_pericias.Enganação = 2
            personagem_pericias.Furtividade = 2
        elif antecedentes == 'Eremita':
            personagem_pericias.Medicina = 2
            personagem_pericias.Religião = 2
        elif antecedentes == 'Forasteiro':
            personagem_pericias.Atletismo = 2
            personagem_pericias.Sobrevivência = 2
        elif antecedentes == 'Heroi do povo':
            personagem_pericias.Manusear_Animais = 2
            personagem_pericias.Sobrevivência = 2
        elif antecedentes == 'Marinheiro':
            personagem_pericias.Percepção = 2
            personagem_pericias.Atletismo = 2
        elif antecedentes == 'Nobre':
            personagem_pericias.História = 2
            personagem_pericias.Persuasão = 2
        elif antecedentes == 'Sábio':
            personagem_pericias.História = 2
            personagem_pericias.Arcanismo = 2
        elif antecedentes == 'Soldado':
            personagem_pericias.Atletismo = 2
            personagem_pericias.Intimidação = 2

        personagem_pericias.save()

        return redirect('escolher_pericias', personagem_id=personagem.id_personagem)


    context = {
        'personagem': personagem,
    }

    return render(request, 'escolher_antecedentes.html', context)

def escolher_caracteristicas(request, personagem_id):

    personagem = get_object_or_404(Personagem, id_personagem=personagem_id)

    if request.method == 'POST':

        nome = request.POST.get('texto_nome')
        descricao = request.POST.get('texto_descricao')

        personagem.nome = nome
        personagem.descricao = descricao

        personagem.save()

    context = {
        'personagem': personagem,
    }

    return render(request, 'escolher_caracteristicas.html', context)