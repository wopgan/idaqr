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


class idaObra(models.Model):
    class Meta:
        verbose_name = "IdaQr Obra"
        verbose_name_plural = "IdaQr Obras"

    obra = models.CharField(max_length=100, verbose_name="Obra: ")
    comando_positivo = models.CharField(max_length=50, verbose_name="Comando Positivo: ")
    comando_negativo = models.CharField(max_length=50, verbose_name="Comando Negativo: ")
    descricao_obra = models.TextField(default='.', verbose_name="Descrição da Obra")
    audio = models.FileField(upload_to='static/', verbose_name='Arquivo de audio OGG')
    video = models.FileField(upload_to='static/', verbose_name='Arquivo de video')

    def __str__(self):
        return self.obra
    
class idaSubComandos(models.Model):
    class Meta:
        verbose_name = "IdaQr Subcomando"
        verbose_name_plural = "IdaQr Subcomandos"

    descricoes = models.ForeignKey(idaObra, on_delete=models.CASCADE)
    sub_comando = models.CharField(max_length=50)
    audio = models.FileField(upload_to='static/', verbose_name='Arquivo de audio OGG subcomando')

    def __str__(self):
        return self.sub_comando