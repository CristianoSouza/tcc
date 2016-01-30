# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academicManager', '0003_arduino'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='arduino',
            field=models.ForeignKey(default=1, to='academicManager.Arduino'),
            preserve_default=False,
        ),
    ]
