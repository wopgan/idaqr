from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IdaDialogSerializer
from .models import listDiolog


class IdaDialogViewSet(viewsets.ModelViewSet):
    queryset = listDiolog.objects.all()
    serializer_class = IdaDialogSerializer
