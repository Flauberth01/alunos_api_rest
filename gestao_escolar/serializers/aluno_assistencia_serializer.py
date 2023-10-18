from rest_framework import serializers

from gestao_escolar.models.aluno_assistencia import AlunoAssistencia


class AlunoAssistenciaSerializer(serializers.ModelSerializer):
    """Serializador para os dados de assistência de aluno"""

    class Meta:
        model = AlunoAssistencia
        exclude = ['aluno']
