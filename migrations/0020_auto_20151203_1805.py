# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_events', '0019_auto_20150804_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='language_code',
            field=models.CharField(default=b'en', max_length=32, choices=[(b'en', b'en')]),
            preserve_default=True,
        ),
    ]
