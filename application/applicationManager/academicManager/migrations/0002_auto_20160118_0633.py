# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academicManager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='data_horario_fim',
        ),
        migrations.RemoveField(
            model_name='aula',
            name='data_horario_inicio',
        ),
        migrations.RemoveField(
            model_name='chamada',
            name='data_horario_leitura',
        ),
        migrations.AddField(
            model_name='aula',
            name='data',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aula',
            name='horario_fim',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='aula',
            name='horario_inicio',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='chamada',
            name='horario_leitura',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
