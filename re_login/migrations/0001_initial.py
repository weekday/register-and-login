# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=32, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('password', models.CharField(max_length=32, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('email', models.EmailField(max_length=254, verbose_name=b'\xe6\xb3\xa8\xe5\x86\x8c\xe9\x82\xae\xe7\xae\xb1')),
                ('phone_number', models.CharField(max_length=14, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d\xe5\x8f\xb7\xe7\xa0\x81')),
            ],
        ),
    ]
