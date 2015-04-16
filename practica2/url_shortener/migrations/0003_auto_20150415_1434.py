# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0002_auto_20150415_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='longUrl',
            field=models.CharField(max_length=300),
            preserve_default=True,
        ),
    ]
