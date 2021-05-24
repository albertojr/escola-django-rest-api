from django.db.models import query
from rest_framework import generics, mixins
from rest_framework.generics import get_object_or_404

#api V2
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response, responses
from rest_framework import mixins

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

"""
    API Versão 1
"""

# listar uma coleção e criar uma objeto sem precisar do ID
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


# Aqui precisa de ID para para atulizar/deletar
# se atentear ao plural e singular
class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    #sobreescrevendo métodos para utlizar
    #pk customizada
    #kwargs pega todos os parametros passados pela URl
    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(),
                                    curso_id=self.kwargs.get('curso_pk'),
                                    pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))

"""
    API versão 2
"""

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
    #modificando viewset para adicionar operações
    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 1
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        #filtrar avaliacoes por curso
        # curso = self.get_object()
        # serializer = AvaliacaoSerializer(curso.avaliacoes.all(),many=True)
        serializer = AvaliacaoSerializer(avaliacoes,many=True)

        return Response(serializer.data)

"""
class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
"""


"""
Limitando as funções do CRUD do viewset
"""
class AvaliacaoViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    #mixins.DestroyModelMixin,
    viewsets.GenericViewSet
    ):

    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer