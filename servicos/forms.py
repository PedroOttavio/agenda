from django import forms
from django.forms import inlineformset_factory

from produtosservico.models import ProdutosServico
from .models import Servico


class ServicoModelForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['nome', 'descricao','preco']

        error_messages = {
            'nome': {'required': 'O nome do serviço é um campo obrigatorio', 'unique': 'Serviço já cadastrado'},
            'descricao':{'required':'A descrição do serviço é um campo obrigatorio'},
            'preco':{'required':'O preço do serviço é um campo obrigatorio'}
        }

ProdutosServicoInLine = inlineformset_factory(Servico, ProdutosServico, fk_name='servico',
                                              fields=('produto', 'quantidade'),extra=1, can_delete= True)

# class Servico(models.Model):
#     nome = models.CharField(max_length=100, help_text='Nome completo do serviço', unique=True)   #slide 10 - verificar erro
#     preco = models.DecimalField(max_digits=5, decimal_places=2, help_text='Preço do serviço')
#     descricao = models.TextField('Descrição', max_length=300, help_text='Descrição e observação do serviço')
#
