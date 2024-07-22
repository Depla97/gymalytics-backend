# Generated by Django 5.0.7 on 2024-07-22 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymsessionsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('preferred_category', models.CharField(blank=True, max_length=255)),
                ('weight', models.IntegerField(blank=True)),
                ('level', models.CharField(blank=True, max_length=255)),
                ('profile_picture_url', models.CharField(blank=True, max_length=1023)),
            ],
        ),
        migrations.RemoveField(
            model_name='set',
            name='user',
        ),
        migrations.RemoveField(
            model_name='session',
            name='user',
        ),
        migrations.AddField(
            model_name='session',
            name='athlete',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gymsessionsapp.athlete'),
        ),
        migrations.AddField(
            model_name='set',
            name='athlete',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gymsessionsapp.athlete'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]