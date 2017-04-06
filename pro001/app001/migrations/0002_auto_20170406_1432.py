# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app001', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.TextField(),
        ),
    ]
