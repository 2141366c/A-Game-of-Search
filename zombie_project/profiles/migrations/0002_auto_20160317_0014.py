# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('survivor', models.IntegerField(default=0)),
                ('killer', models.IntegerField(default=0)),
                ('stamina', models.IntegerField(default=0)),
                ('party', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zombies_killed', models.IntegerField(default=0)),
                ('ammo', models.IntegerField(default=0)),
                ('food', models.IntegerField(default=10)),
                ('days_alive', models.IntegerField(default=0)),
                ('party_size', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='player',
            old_name='name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='player',
            name='ammo',
        ),
        migrations.RemoveField(
            model_name='player',
            name='days_alive',
        ),
        migrations.RemoveField(
            model_name='player',
            name='food',
        ),
        migrations.RemoveField(
            model_name='player',
            name='zombies_killed',
        ),
        migrations.AddField(
            model_name='player',
            name='badges',
            field=models.ForeignKey(default=1, to='profiles.Badges'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='status',
            field=models.ForeignKey(default=1, to='profiles.Status'),
            preserve_default=False,
        ),
    ]
