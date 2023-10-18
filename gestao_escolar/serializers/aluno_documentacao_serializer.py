from rest_framework import serializers

from gestao_escolar.models.aluno_documentacao import AlunoDocumentacao


class AlunoDocumentacaoSerializer(serializers.ModelSerializer):
    """Serializador para os dados de documentação de aluno"""
    
    class Meta:
        model = AlunoDocumentacao
        exclude = ['aluno']