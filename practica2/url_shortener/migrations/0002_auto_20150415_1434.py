# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='url',
            old_name='longurl',
            new_name='longUrl',
        ),
    ]
