# Generated by Django 4.2.1 on 2023-05-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ida_dialog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listdiolog',
            name='keywordNarrative',
            field=models.FileField(upload_to='static/', verbose_name='Arquivo de audio OGG'),
        ),
    ]
