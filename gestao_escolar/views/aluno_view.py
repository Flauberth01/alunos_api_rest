from rest_framework import viewsets

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.serializers.aluno_serializer import AlunoSerializer, AlunoComDependenciasSerializer


class AlunoViewSet(viewsets.ModelViewSet):
    """Lida com a criação, visualização e edição de aluno, cria aluno junto com suas dependências"""
    
    queryset = Aluno.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create':
            return AlunoComDependenciasSerializer
        return AlunoSerializer
