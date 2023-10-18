from rest_framework import serializers

from gestao_escolar.models.aluno_saude import AlunoSaude


class AlunoSaudeSerializer(serializers.ModelSerializer):
    """Serializador para os dados de saúde de aluno"""
   
    class Meta:
        model = AlunoSaude
        exclude = ['aluno']