from rest_framework import generics
from rest_framework.exceptions import NotFound

from gestao_escolar.models.aluno_responsavel import AlunoResponsavel
from gestao_escolar.models.aluno import Aluno
from gestao_escolar.serializers.aluno_responsavel_serializer import AlunoResponsavelSerializer


class AlunoResponsavelRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Exibe ou atualiza o responsável de um aluno"""

    serializer_class = AlunoResponsavelSerializer

    def get_object(self):
        aluno_id = self.kwargs['aluno_id']
        try:
            aluno = Aluno.objects.get(id=aluno_id)
            return AlunoResponsavel.objects.get(aluno=aluno, responsavel_designado=True)
        except Aluno.DoesNotExist:
            raise NotFound(detail='Não existem dados de aluno para o id informado.')
        except AlunoResponsavel.DoesNotExist:
            raise NotFound(detail='Não existem dados de responsável para o id informado.')
        except AlunoResponsavel.MultipleObjectsReturned:
            raise NotFound(detail='Há mais de um responsável com o mesmo id informado.')