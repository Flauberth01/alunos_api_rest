from rest_framework import serializers

from gestao_escolar.models.aluno_transporte import AlunoTransporte


class AlunoTransporteSerializer(serializers.ModelSerializer):
    """Serializador para os dados de transporte de aluno"""

    class Meta:
        model = AlunoTransporte
        exclude = ['aluno']