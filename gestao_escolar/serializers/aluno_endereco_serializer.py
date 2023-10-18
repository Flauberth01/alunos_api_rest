from rest_framework import serializers

from gestao_escolar.models.aluno_endereco import AlunoEndereco


class AlunoEnderecoSerializer(serializers.ModelSerializer):
    """Serializador para os dados de endereço de aluno"""
    
    class Meta:
        model = AlunoEndereco
        exclude = ['aluno']