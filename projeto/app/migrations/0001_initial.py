# Generated by Django 5.1 on 2024-09-22 20:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Magia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nivel', models.IntegerField()),
                ('descricao', models.TextField()),
                ('tipo_dado', models.IntegerField(null=True)),
                ('quant_dado', models.IntegerField(null=True)),
                ('alcance', models.IntegerField(null=True)),
                ('duracao', models.CharField(max_length=100, null=True)),
                ('tempo_conjuracao', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Magia_Preparada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_teste.magia')),
            ],
        ),
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id_personagem', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=15000)),
                ('nivel', models.IntegerField()),
                ('experiencia', models.IntegerField(default=0)),
                ('raca', models.CharField(max_length=50)),
                ('classes', models.JSONField(default=dict)),
                ('pontos_magia', models.JSONField(default=dict)),
                ('pontos_magia_atual', models.JSONField(default=dict)),
                ('bonus_proeficiencia', models.IntegerField(default=0)),
                ('vida_maxima', models.IntegerField(default=0)),
                ('vida_atual', models.IntegerField(default=0)),
                ('dado_vida', models.IntegerField(default=0)),
                ('resistencias', models.CharField(blank=True, default=' ', max_length=255, null=True)),
                ('vulnerabilidades', models.CharField(blank=True, default=' ', max_length=255, null=True)),
                ('armadura', models.IntegerField(default=10)),
                ('iniciativa', models.IntegerField(default=0)),
                ('velocidade', models.IntegerField(default=0)),
                ('sabedoria_pasiva', models.IntegerField(default=0)),
                ('percepcao_pasiva', models.IntegerField(default=0)),
                ('antecedentes', models.CharField(blank=True, default=' ', max_length=50, null=True)),
                ('magias', models.ManyToManyField(related_name='personagens', to='app_teste.magia')),
                ('magias_preparadas', models.ManyToManyField(related_name='personagens', to='app_teste.magia_preparada')),
            ],
        ),
        migrations.CreateModel(
            name='Pericias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acrobacia', models.IntegerField(default=0)),
                ('Atletismo', models.IntegerField(default=0)),
                ('Atuação', models.IntegerField(default=0)),
                ('Arcanismo', models.IntegerField(default=0)),
                ('Enganação', models.IntegerField(default=0)),
                ('Furtividade', models.IntegerField(default=0)),
                ('História', models.IntegerField(default=0)),
                ('Intimidação', models.IntegerField(default=0)),
                ('Intuição', models.IntegerField(default=0)),
                ('Investigação', models.IntegerField(default=0)),
                ('Manusear_Animais', models.IntegerField(default=0)),
                ('Medicina', models.IntegerField(default=0)),
                ('Natureza', models.IntegerField(default=0)),
                ('Percepção', models.IntegerField(default=0)),
                ('Persuasão', models.IntegerField(default=0)),
                ('Prestidigitação', models.IntegerField(default=0)),
                ('Religião', models.IntegerField(default=0)),
                ('Sobrevivência', models.IntegerField(default=0)),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='percias', to='app_teste.personagem')),
            ],
        ),
        migrations.AddField(
            model_name='magia_preparada',
            name='personagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_teste.personagem'),
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forca', models.IntegerField(default=0)),
                ('destreza', models.IntegerField(default=0)),
                ('constituicao', models.IntegerField(default=0)),
                ('inteligencia', models.IntegerField(default=0)),
                ('sabedoria', models.IntegerField(default=0)),
                ('carisma', models.IntegerField(default=0)),
                ('personagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habilidades', to='app_teste.personagem')),
            ],
        ),
    ]
