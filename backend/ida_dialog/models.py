from django.db import models

# Create your models here.
class listDiolog(models.Model):
    class Meta:
        verbose_name = "IdaQr Dado"
        verbose_name_plural = "IdaQr Dados"

    keyTitle = models.CharField(max_length=100, verbose_name='Titulo da Obra')
    keywordVideo = models.FileField(upload_to='static/', verbose_name='Arquivo de video')
    keywordName = models.CharField(max_length=50, verbose_name='Comando')
    keywordNarrative = models.FileField(upload_to='static/', verbose_name='Arquivo de audio OGG')
    keywordSpeech = models.TextField(verbose_name='Instruções de Sequência')

    def __str__(self):
        return self.keywordName
