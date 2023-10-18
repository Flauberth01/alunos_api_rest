from rest_framework import generics
from rest_framework.exceptions import NotFound

from gestao_escolar.models.aluno_responsavel import AlunoResponsavel
from gestao_escolar.models.aluno import Aluno
from gestao_escolar.serializers.aluno_responsavel_serializer import AlunoResponsavelSerializer


class AlunoFiliacoesRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Exibe ou atualiza as filiações de um aluno"""

    serializer_class = AlunoResponsavelSerializer

    def get_object(self):
        aluno_id = self.kwargs['aluno_id']
        filiacao = self.kwargs['filiacao']
        try:
            aluno = Aluno.objects.get(id=aluno_id)
        except Aluno.DoesNotExist:
            raise NotFound(detail='Não existem dados de aluno para o id informado.')
        try:
            if filiacao == 1:
                responsavel = AlunoResponsavel.objects.get(aluno=aluno, filiacao1=True)
            elif filiacao == 2:
                responsavel = AlunoResponsavel.objects.get(aluno=aluno, filiacao2=True)
            else:
                raise NotFound(detail='O número de filiação fornecido deve ser 1 ou 2.')
            return responsavel
        except AlunoResponsavel.DoesNotExist:
            raise NotFound(detail=f'Não existem dados de filiação {filiacao} para o id informado.')
        