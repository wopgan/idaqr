from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IdaStartSerializer, IdaInicioSerializer
from .models import idaStart, idaInicio


class IdaStartView(viewsets.ModelViewSet):
    queryset = idaStart.objects.all()
    serializer_class = IdaStartSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return listDiolog.objects.filter(keywordName__icontains=query)
        return listDiolog.objects.all()
    

class IdaInicioViewSet(viewsets.ModelViewSet):
    queryset = idaInicio.objects.all()
    serializer_class = IdaInicioSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return idaInicio.objects.filter(titulo=query)
        return idaInicio.objects.all()
