from rest_framework import serializers

from .models import Curso,Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        #campo email, não vai ser apresentando quando alguém
        #consultar a avaliação. Só vai ver na hora de cadastrar
        extra_kwargs = {
            'email': {'write_only':True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criacao',
            'ativo',
        )
    
    def validate_avaliacao(self,valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError("A avaliação precisa ser um inteiro entre 1 e 5")


class CursoSerializer(serializers.ModelSerializer):
    # Nested relationship
    #recomendado para relacionamento 1 para 1:
    # avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    # HyperLinked Related Field
    # Oference links para acessar os dados extras, caso o cliente queira
    # avaliacoes = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='avaliacao-detail'
    # )
   
    #primary key rekated field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model =  Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        )