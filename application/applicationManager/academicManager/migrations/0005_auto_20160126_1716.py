# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academicManager', '0004_aula_arduino'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('bloco', models.CharField(max_length=200)),
                ('espaco', models.CharField(max_length=200)),
                ('sala', models.CharField(max_length=200)),
                ('arduino', models.ForeignKey(to='academicManager.Arduino')),
            ],
        ),
        migrations.RemoveField(
            model_name='aula',
            name='arduino',
        ),
    ]
