# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('milage', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(related_name='car_barnd', to='home.Brand')),
            ],
        ),
    ]
