from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import IdaDialogSerializer, IdaObraSerializer, IdaSubComandosSerializer
from .models import listDiolog, idaObra, idaSubComandos


class IdaDialogViewSet(viewsets.ModelViewSet):
    queryset = listDiolog.objects.all()
    serializer_class = IdaDialogSerializer

    def get_queryset(self):
        keyword_name = self.request.query_params.get('q')
        queryset = listDiolog.objects.all()
        if keyword_name:
            queryset = queryset.filter(keywordName=keyword_name)
        return queryset

    def list(self, request):
        keyword_name = self.request.query_params.get('q')
        if not keyword_name:
            return super().list(request)
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            return Response({'error': 'Comando não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IdaDialogSerializer(obj)
        return Response(serializer.data)
    
class IdaObraViewSet(viewsets.ModelViewSet):
    queryset = idaObra.objects.all()
    serializer_class = IdaObraSerializer

    def get_queryset(self):
        obra_name = self.request.query_params.get('q')
        queryset = idaObra.objects.all()
        if obra_name:
            queryset = queryset.filter(palavra_chave=obra_name)
        return queryset
    
    def list(self, request):
        obra_name = self.request.query_params.get('q')
        if not obra_name:
            return super().list(request)
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            return Response({'error': 'Comando não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IdaObraSerializer(obj)
        return Response(serializer.data)
    

class IdaSubComandoViewSet(viewsets.ModelViewSet):
    queryset = idaSubComandos.objects.all()
    serializer_class = IdaSubComandosSerializer

    def get_queryset(self):
        comando_name = self.request.query_params.get('q')
        queryset = idaSubComandos.objects.all()
        if comando_name:
            queryset = queryset.filter(sub_comando=comando_name)
        return queryset
    
    def list(self, request):
        comando_name = self.request.query_params.get('q')
        if not comando_name:
            return super().list(request)
        queryset = self.get_queryset()
        obj = queryset.first()
        if not obj:
            return Response({'error': 'Comando não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = IdaSubComandosSerializer(obj)
        return Response(serializer.data)

    