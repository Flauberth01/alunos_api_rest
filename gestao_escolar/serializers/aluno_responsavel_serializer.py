from rest_framework import serializers

from gestao_escolar.models.aluno_responsavel import AlunoResponsavel


class AlunoResponsavelSerializer(serializers.ModelSerializer):
    """Serializador para os dados do responsável do aluno"""
    
    class Meta:
        model = AlunoResponsavel
        exclude = ['aluno']