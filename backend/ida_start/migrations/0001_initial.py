# Generated by Django 4.2.1 on 2023-05-06 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='idaStart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startSound', models.FileField(upload_to='media/', verbose_name='Audio tela inicial')),
            ],
        ),
    ]
