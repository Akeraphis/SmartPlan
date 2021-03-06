# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DataLayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.Company')),
            ],
        ),
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creationDate', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updateDate', models.DateTimeField(auto_now=True, verbose_name='Last Update Date')),
                ('dataLayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.DataLayer')),
            ],
        ),
    ]
