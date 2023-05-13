from rest_framework import serializers
from .models import idaStart, idaInicio

class IdaStartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = idaStart
        fields = ['id', 'startSound']

class IdaInicioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = idaInicio
        fields = ['id', 'titulo', 'texto', 'audio_text', 'audio_start']
