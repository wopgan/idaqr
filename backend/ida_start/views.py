from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IdaInicioSerializer
from .models import idaInicio


class IdaInicioViewSet(viewsets.ModelViewSet):
    queryset = idaInicio.objects.all()
    serializer_class = IdaInicioSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return idaInicio.objects.filter(titulo=query)
        return idaInicio.objects.all()
