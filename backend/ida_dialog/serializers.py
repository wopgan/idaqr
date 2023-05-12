from rest_framework import serializers
from .models import listDiolog, idaObra, idaSubComandos

class IdaDialogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = listDiolog
        fields = ['id', 'keywordName', 'keyTitle', 'keywordVideo' ,'keywordNarrative', 'keywordSpeech']

class IdaObraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = idaObra
        fields = ['obra', 'comando_positivo', 'comando_negativo', 'audio', 'video']

class IdaSubComandosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = idaSubComandos
        fields = ['descricoes', 'sub_comando', 'audio']