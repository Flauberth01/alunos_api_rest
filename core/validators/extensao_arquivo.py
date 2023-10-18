import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_extensao_arquivo(value):
    extensao = os.path.splitext(value.name)[1]
    extensoes_validas = ['.pdf', '.doc', '.docx', '.jpg', '.png']
    if not extensao.lower() in extensoes_validas:
        raise ValidationError('Formato inválido. Insira um arquivo no formato .pdf, .doc, .docx, .jpg, .jpeg, ou .png.')
    
def validate_extensao_imagem(value):
    extensao = os.path.splitext(value.name)[1]
    extensoes_validas = ['.jpg', '.jpeg', '.png']
    if not extensao.lower() in extensoes_validas:
        raise ValidationError('Formato inválido. Insira um arquivo no formato .jpg, .jpeg, ou .png.')
    