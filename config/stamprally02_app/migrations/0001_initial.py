# Generated by Django 4.0.2 on 2022-02-13 00:08

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Border',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('n03_001', models.CharField(max_length=10, verbose_name='都道府県名')),
                ('n03_002', models.CharField(blank=True, max_length=20, verbose_name='支庁名')),
                ('n03_003', models.CharField(blank=True, max_length=20, verbose_name='群・政令市名')),
                ('n03_004', models.CharField(blank=True, max_length=20, verbose_name='市区町村名')),
                ('n03_007', models.CharField(max_length=5, verbose_name='行政区域コード')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4612)),
            ],
            options={
                'verbose_name': '行政区域',
                'verbose_name_plural': '行政区域一覧',
            },
        ),
    ]
