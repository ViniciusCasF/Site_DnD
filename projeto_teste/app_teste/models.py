from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

class Magia(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField()
    descricao = models.TextField()
    tipo_dado = models.IntegerField(null=True)
    quant_dado = models.IntegerField(null=True)
    alcance = models.IntegerField(null=True)
    duracao = models.CharField(max_length=100, null=True)
    tempo_conjuracao = models.CharField(max_length=50, null=True)

class Magia_Preparada(models.Model):
    personagem = models.ForeignKey('Personagem', on_delete=models.CASCADE)
    magia = models.ForeignKey('Magia', on_delete=models.CASCADE)

class Personagem(models.Model):
    id_personagem = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=15000)
    nivel = models.IntegerField()
    experiencia = models.IntegerField(default=0)
    raca = models.CharField(max_length=50)

    classes = models.JSONField(default=dict)# classe1 : (barbaro, mago ...)

    pontos_magia = models.JSONField(default=dict) # pontos_magia1 : (quantidade de pontos de magia)
    pontos_magia_atual = models.JSONField(default=dict) #pontos_magia1 : (Varia com o gasto)

    bonus_proeficiencia = models.IntegerField(default=0)
    vida_maxima = models.IntegerField(default=0)
    vida_atual = models.IntegerField(default=0)
    dado_vida = models.IntegerField(default=0)
    resistencias = models.CharField(max_length=255, null=True, blank=True, default=' ')
    vulnerabilidades = models.CharField(max_length=255, null=True, blank=True, default=' ')
    armadura = models.IntegerField(default=10)
    iniciativa = models.IntegerField(default=0)
    velocidade = models.IntegerField(default=0)
    sabedoria_pasiva = models.IntegerField(default=0)
    percepcao_pasiva = models.IntegerField(default=0)
    antecedentes = models.CharField(max_length=50, null=True, blank=True, default=' ')

    magias = models.ManyToManyField(Magia, related_name="personagens")
    magias_preparadas = models.ManyToManyField(Magia_Preparada, related_name="personagens")

class Habilidades(models.Model):
    forca = models.IntegerField(default=0)
    destreza = models.IntegerField(default=0)
    constituicao = models.IntegerField(default=0)
    inteligencia = models.IntegerField(default=0)
    sabedoria = models.IntegerField(default=0)
    carisma = models.IntegerField(default=0)
    personagem = models.ForeignKey(Personagem, related_name='habilidades', on_delete=models.CASCADE)

class Pericias(models.Model):
    Acrobacia = models.IntegerField(default=0)
    Atletismo = models.IntegerField(default=0)
    Atuação = models.IntegerField(default=0)
    Arcanismo = models.IntegerField(default=0)
    Enganação = models.IntegerField(default=0)
    Furtividade = models.IntegerField(default=0)
    História = models.IntegerField(default=0)
    Intimidação = models.IntegerField(default=0)
    Intuição = models.IntegerField(default=0)
    Investigação = models.IntegerField(default=0)
    Manusear_Animais = models.IntegerField(default=0)
    Medicina = models.IntegerField(default=0)
    Natureza = models.IntegerField(default=0)
    Percepção = models.IntegerField(default=0)
    Persuasão = models.IntegerField(default=0)
    Prestidigitação = models.IntegerField(default=0)
    Religião = models.IntegerField(default=0)
    Sobrevivência = models.IntegerField(default=0)
    personagem = models.ForeignKey(Personagem, related_name='percias', on_delete=models.CASCADE)