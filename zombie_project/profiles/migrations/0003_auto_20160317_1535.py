# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160317_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='badges',
        ),
        migrations.DeleteModel(
            name='Badges',
        ),
        migrations.RemoveField(
            model_name='player',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
        migrations.AddField(
            model_name='player',
            name='ammo',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='daysAlive',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='food',
            field=models.IntegerField(default=3),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='killerBadge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='partyBadge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='partySize',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='staminaBadge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='survivorBadge',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='player',
            name='zombiesKilled',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
