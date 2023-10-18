from rest_framework import generics
from rest_framework.exceptions import NotFound

from gestao_escolar.models.aluno_endereco import AlunoEndereco
from gestao_escolar.serializers.aluno_endereco_serializer import AlunoEnderecoSerializer


class AlunoEnderecoRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Exibe ou atualiza um endereço de aluno"""

    serializer_class = AlunoEnderecoSerializer

    def get_object(self):
        aluno_id = self.kwargs['aluno_id']
        try:
            return AlunoEndereco.objects.get(aluno_id=aluno_id)
        except AlunoEndereco.DoesNotExist:
            raise NotFound(detail='Não existem dados de endereço para o id informado.')
