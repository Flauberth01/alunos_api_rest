from rest_framework import generics
from rest_framework.exceptions import NotFound

from gestao_escolar.models.aluno_transporte import AlunoTransporte
from gestao_escolar.serializers.aluno_transporte_serializer import AlunoTransporteSerializer


class AlunoTransporteRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Exibe ou atualiza os dados de transporte de um aluno"""

    serializer_class = AlunoTransporteSerializer

    def get_object(self):
        aluno_id = self.kwargs['aluno_id']
        try:
            return AlunoTransporte.objects.get(aluno_id=aluno_id)
        except AlunoTransporte.DoesNotExist:
            raise NotFound(detail='Não existem dados de transporte para o id informado.')