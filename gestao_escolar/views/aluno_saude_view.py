from rest_framework import generics
from rest_framework.exceptions import NotFound

from gestao_escolar.models.aluno_saude import AlunoSaude
from gestao_escolar.serializers.aluno_saude_serializer import AlunoSaudeSerializer


class AlunoSaudeRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Exibe ou atualiza os dados de saúde de um aluno"""

    serializer_class = AlunoSaudeSerializer

    def get_object(self):
        aluno_id = self.kwargs['aluno_id']
        try:
            return AlunoSaude.objects.get(aluno_id=aluno_id)
        except AlunoSaude.DoesNotExist:
            raise NotFound(detail='Não existem dados de saúde para o id informado.')