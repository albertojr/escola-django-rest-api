from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso,Avaliacao
from .serializers import CursoSerializer,AvaliacaoSerializer


class CursoAPIView(APIView):
    """
    API de Cursos Udemy
    """

    def get(self,request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos,many=True)
        return Response(serializer.data)
    

    def post(self, request):
        #Pegando dados da requisição para criar o curso e serializar
        serializer = CursoSerializer(data=request.data)
        # Verifica se os dados são válidos
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data,status=status.HTTP_201_CREATED)

class AvaliacaoAPIView(APIView):
    """
    API de avaliações
    """
    def get(self,request):
        avalicaoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avalicaoes,many=True)
        #gerando JSON
        return Response(serializer.data)
    

    def post(self, request):
        serializer = AvaliacaoSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        return Response(serializer.data,status = status.HTTP_201_CREATED)