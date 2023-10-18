from rest_framework import generics
from rest_framework.exceptions import NotFound

from gestao_escolar.models.aluno_documentacao import AlunoDocumentacao
from gestao_escolar.serializers.aluno_documentacao_serializer import AlunoDocumentacaoSerializer


class AlunoDocumentacaoRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Exibe ou atualiza a documentação de um aluno"""

    serializer_class = AlunoDocumentacaoSerializer

    def get_object(self):
        aluno_id = self.kwargs['aluno_id']
        try:
            return AlunoDocumentacao.objects.get(aluno_id=aluno_id)
        except AlunoDocumentacao.DoesNotExist:
            raise NotFound(detail='Não existem dados de documentação para o id informado.')