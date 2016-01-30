# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academicManager', '0005_auto_20160126_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='sala',
            field=models.ForeignKey(to='academicManager.Sala', default=1),
            preserve_default=False,
        ),
    ]
