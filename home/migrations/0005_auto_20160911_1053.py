# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160911_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(),
        ),
    ]
