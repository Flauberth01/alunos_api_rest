from django.db import transaction
from rest_framework import serializers

from gestao_escolar.models.aluno import Aluno
from gestao_escolar.models.aluno_documentacao import AlunoDocumentacao
from gestao_escolar.models.aluno_responsavel import AlunoResponsavel
from gestao_escolar.models.aluno_endereco import AlunoEndereco
from gestao_escolar.models.aluno_saude import AlunoSaude
from gestao_escolar.models.aluno_assistencia import AlunoAssistencia
from gestao_escolar.models.aluno_transporte import AlunoTransporte
from gestao_escolar.serializers.aluno_documentacao_serializer import AlunoDocumentacaoSerializer
from gestao_escolar.serializers.aluno_responsavel_serializer import AlunoResponsavelSerializer
from gestao_escolar.serializers.aluno_endereco_serializer import AlunoEnderecoSerializer
from gestao_escolar.serializers.aluno_saude_serializer import AlunoSaudeSerializer
from gestao_escolar.serializers.aluno_assistencia_serializer import AlunoAssistenciaSerializer
from gestao_escolar.serializers.aluno_transporte_serializer import AlunoTransporteSerializer


class AlunoSerializer(serializers.ModelSerializer):
    """Serializador para o model Aluno"""

    class Meta:
        model = Aluno
        fields = '__all__'


class AlunoComDependenciasSerializer(serializers.ModelSerializer):
    """Serializador para os models Aluno, AlunoDocumentacao , AlunoResponsavel, AlunoEndereco, AlunoSaude, AlunoAssistencia e AlunoTransporte"""

    documentacao = AlunoDocumentacaoSerializer()
    responsaveis = AlunoResponsavelSerializer(many=True)
    endereco = AlunoEnderecoSerializer()
    saude = AlunoSaudeSerializer(required=False)
    assistencia = AlunoAssistenciaSerializer(required=False)
    transporte = AlunoTransporteSerializer()

    class Meta:
        model = Aluno
        fields = '__all__'
        include = ['documentacao', 'responsaveis', 'endereco', 'saude', 'assistencia', 'transporte']

    @transaction.atomic
    def create(self, validated_data):
        documentacao_data = validated_data.pop('documentacao')
        responsaveis_data = validated_data.pop('responsaveis')
        endereco_data = validated_data.pop('endereco')
        saude_data = validated_data.pop('saude', None)
        assistencia_data = validated_data.pop('assistencia', None)
        transporte_data = validated_data.pop('transporte')

        aluno = Aluno.objects.create(**validated_data)
        AlunoDocumentacao.objects.create(aluno=aluno, **documentacao_data)

        for responsavel_data in responsaveis_data:
            cpf = responsavel_data.get('cpf')
            responsavel = AlunoResponsavel.objects.filter(cpf__iexact=cpf).first() if cpf else None
            if not responsavel:
                responsavel = AlunoResponsavel.objects.create(**responsavel_data)
            responsavel.aluno.add(aluno)

        AlunoEndereco.objects.create(aluno=aluno, **endereco_data)

        if saude_data:
            AlunoSaude.objects.create(aluno=aluno, **saude_data)

        if assistencia_data:
            AlunoAssistencia.objects.create(aluno=aluno, **assistencia_data)

        AlunoTransporte.objects.create(aluno=aluno, **transporte_data)
        return aluno

    def validate(self, data):
        responsaveis = data.get('responsaveis')
        documentacao = data.get('documentacao')
        responsaveis_designados = [r for r in responsaveis if r.get('responsavel_designado')]

        if len(responsaveis_designados) > 1:
            raise serializers.ValidationError('Só pode haver um responsável designado.')

        for responsavel_data in responsaveis:
            if (responsavel_data.get('filiacao1') and responsavel_data.get('filiacao2')) or \
               (responsavel_data.get('filiacao1') or responsavel_data.get('filiacao2')) and responsavel_data.get('parentesco'):
                raise serializers.ValidationError('Parentesco só deve ser informado caso o responsável não seja a filiação 1 ou 2.')

        if documentacao.get('rg') and documentacao.get('rne'):
            raise serializers.ValidationError('Envie apenas um, RG ou RNE.')

        if all(documentacao.get(key) for key in ['cert_antiga_termo', 'cert_antiga_folha', 'cert_antiga_livro']):
            raise serializers.ValidationError('Preencha todos os campos corretamente se for enviar a certidão modelo antigo.')

        if documentacao.get('certidao_nova') and any(documentacao.get(key) for key in ['cert_antiga_termo', 'cert_antiga_folha', 'cert_antiga_livro']):
            raise serializers.ValidationError('Envie apenas um, certidão modelo novo ou antigo.')
        
        return data
