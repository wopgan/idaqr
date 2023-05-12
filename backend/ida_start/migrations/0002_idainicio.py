# Generated by Django 4.2.1 on 2023-05-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ida_start', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='idaInicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo da abertura: ')),
                ('texto', models.CharField(max_length=200, verbose_name='Texto da abertura: ')),
            ],
            options={
                'verbose_name': 'Ida Inicio',
                'verbose_name_plural': 'Ida Inicio',
            },
        ),
    ]
