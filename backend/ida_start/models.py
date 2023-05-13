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
    
class idaInicio(models.Model):
    class Meta:
        verbose_name = "Ida Inicio"
        verbose_name_plural = "Ida Inicio"

    titulo = models.CharField(max_length=50, verbose_name="Titulo da abertura: ")
    texto = models.CharField(max_length=200, verbose_name="Texto da abertura: ")
    audio_text = models.BooleanField(default=False)
    audio_start = models.FileField(upload_to='static/', blank=True)

    def __str__(self):
        return self.texto
    
