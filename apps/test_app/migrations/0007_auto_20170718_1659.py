# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 23:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0006_auto_20170718_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='user',
            name='duration',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.Post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.User'),
        ),
    ]