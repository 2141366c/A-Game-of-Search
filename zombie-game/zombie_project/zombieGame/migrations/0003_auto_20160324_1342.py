# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zombieGame', '0002_auto_20160318_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='killerBadge',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='partyBadge',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='staminaBadge',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='survivorBadge',
            field=models.BooleanField(default=False),
        ),
    ]
