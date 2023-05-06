from django.db import models

# Create your models here.
class idaStart(models.Model):
    class Meta:
        verbose_name = "IdaQr Inicio"
        verbose_name_plural = "IdaQr Inicio"

    titleSound = models.CharField(max_length=50, default='Titulo' ,verbose_name='Titulo da Entrada')
    startSound = models.FileField(upload_to='static/', verbose_name='Audio tela inicial')

    def __str__(self):
        return self.titleSound