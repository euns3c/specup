# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specup', '0002_auto_20170517_1928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_point',
            name='user',
        ),
        migrations.DeleteModel(
            name='Admin_Point',
        ),
    ]
