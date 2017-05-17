# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specup', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin_point',
            name='point_number',
        ),
        migrations.AddField(
            model_name='admin_point',
            name='user',
            field=models.ForeignKey(default=0, to='specup.UserPointHistory'),
            preserve_default=False,
        ),
    ]
