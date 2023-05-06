from django.shortcuts import render
from rest_framework import viewsets
from .serializers import IdaStartSerializer
from .models import idaStart


class IdaStartView(viewsets.ModelViewSet):
    queryset = idaStart.objects.all()
    serializer_class = IdaStartSerializer
