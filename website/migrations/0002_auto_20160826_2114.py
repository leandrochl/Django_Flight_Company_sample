# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='voo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('data_decolagem', models.DateTimeField()),
                ('data_pouso', models.DateTimeField()),
                ('id_origem', models.CharField(max_length=3)),
                ('id_destino', models.CharField(max_length=3)),
                ('preco', models.FloatField()),
                ('assentos_totais', models.IntegerField()),
                ('id_com_aerea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voo_requests_created', to='website.com_aerea')),
            ],
        ),
        migrations.DeleteModel(
            name='cidade',
        ),
    ]
