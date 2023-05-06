from rest_framework import serializers
from .models import listDiolog

class IdaDialogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = listDiolog
        fields = ['id', 'keywordName', 'keyTitle', 'keywordVideo' ,'keywordNarrative', 'keywordSpeech']