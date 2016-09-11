# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20160911_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='milage',
            field=models.FloatField(),
        ),
    ]
