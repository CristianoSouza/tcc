# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=16, blank=True)),
                ('data_nascimento', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('nome_pai', models.CharField(null=True, max_length=200)),
                ('nome_mae', models.CharField(null=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AlunoDisciplina',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('aluno', models.ForeignKey(to='academicManager.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('data_horario_inicio', models.DateTimeField(verbose_name='hora inicio')),
                ('data_horario_fim', models.DateTimeField(verbose_name='hora fim')),
            ],
        ),
        migrations.CreateModel(
            name='Chamada',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('data_horario_leitura', models.DateTimeField(verbose_name='hora leitura')),
                ('presenca', models.CharField(max_length=1, choices=[('P', 'Presença'), ('F', 'Falta')])),
                ('aluno', models.ForeignKey(to='academicManager.Aluno')),
                ('aula', models.ForeignKey(to='academicManager.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('curso', models.ForeignKey(to='academicManager.Curso')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=16, blank=True)),
                ('data_nascimento', models.DateField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rfid',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('rfid_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='professor',
            field=models.ForeignKey(to='academicManager.Professor'),
        ),
        migrations.AddField(
            model_name='aula',
            name='disciplina',
            field=models.ForeignKey(to='academicManager.Disciplina'),
        ),
        migrations.AddField(
            model_name='alunodisciplina',
            name='disciplina',
            field=models.ForeignKey(to='academicManager.Disciplina'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='curso',
            field=models.ForeignKey(to='academicManager.Curso'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='rfid_code',
            field=models.ForeignKey(to='academicManager.Rfid'),
        ),
    ]
