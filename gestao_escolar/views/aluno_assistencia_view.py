from rest_framework import generics
from rest_framework.exceptions import NotFound

from gestao_escolar.models.aluno_assistencia import AlunoAssistencia
from gestao_escolar.serializers.aluno_assistencia_serializer import AlunoAssistenciaSerializer


class AlunoAssistenciaRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Exibe ou atualiza os dados de assistência de um aluno"""

    serializer_class = AlunoAssistenciaSerializer

    def get_object(self):
        aluno_id = self.kwargs['aluno_id']
        try:
            return AlunoAssistencia.objects.get(aluno_id=aluno_id)
        except AlunoAssistencia.DoesNotExist:
            raise NotFound(detail='Não existem dados de assistência para o id informado.')