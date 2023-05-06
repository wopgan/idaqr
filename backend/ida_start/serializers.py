from rest_framework import serializers
from .models import idaStart

class IdaStartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = idaStart
        fields = ['id', 'startSound']
