# Generated by Django 4.2.1 on 2023-05-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ida_dialog', '0002_idaobra_idasubcomandos'),
    ]

    operations = [
        migrations.AddField(
            model_name='idaobra',
            name='descricao_obra',
            field=models.TextField(default='.'),
        ),
    ]
