from django.urls import path, include
from rest_framework import routers

from gestao_escolar.views.aluno_view import AlunoViewSet
from gestao_escolar.views.aluno_documentacao_view import AlunoDocumentacaoRetrieveUpdate
from gestao_escolar.views.aluno_responsavel_view import AlunoResponsavelRetrieveUpdate
from gestao_escolar.views.aluno_filiacoes_view import AlunoFiliacoesRetrieveUpdate
from gestao_escolar.views.aluno_endereco_view import AlunoEnderecoRetrieveUpdate
from gestao_escolar.views.aluno_saude_view import AlunoSaudeRetrieveUpdate
from gestao_escolar.views.aluno_assistencia_view import AlunoAssistenciaRetrieveUpdate
from gestao_escolar.views.aluno_transporte_view import AlunoTransporteRetrieveUpdate

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet, basename='alunos')

urlpatterns = [
    path('', include(router.urls)),
    path('alunos/<int:aluno_id>/documentacao', AlunoDocumentacaoRetrieveUpdate.as_view(), name='aluno_documentacao'),
    path('alunos/<int:aluno_id>/responsavel', AlunoResponsavelRetrieveUpdate.as_view(), name='aluno_responsavel'),
    path('alunos/<int:aluno_id>/filiacoes/<int:filiacao>', AlunoFiliacoesRetrieveUpdate.as_view(), name='aluno_filiacoes'),
    path('alunos/<int:aluno_id>/endereco', AlunoEnderecoRetrieveUpdate.as_view(), name='aluno_endereco'),
    path('alunos/<int:aluno_id>/saude', AlunoSaudeRetrieveUpdate.as_view(), name='aluno_saude'),
    path('alunos/<int:aluno_id>/assistencia', AlunoAssistenciaRetrieveUpdate.as_view(), name='aluno_assistencia'),
    path('alunos/<int:aluno_id>/transporte', AlunoTransporteRetrieveUpdate.as_view(), name='aluno_transporte'),
]