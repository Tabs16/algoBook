# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('badges', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.Badges')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]