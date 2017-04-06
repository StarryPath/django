# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title',models.TextField(verbose_name='title',serialize=False,auto_created=False,primary_key=False)),
                ('content',models.TextField(verbose_name='content',serialize=False,auto_created=False,primary_key=False)),
            ],
        ),
    ]
