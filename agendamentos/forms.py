from django import forms


from .models import Agendamento
from clientes.models import Cliente
from funcionarios.models import Funcionario



class AgendamentoListForm(forms.Form):

    cliente = forms.ModelChoiceField(label='Cliente', queryset=Cliente.objects.all(), required=False)
    funcionario = forms.ModelChoiceField(label='Funcionario', queryset=Funcionario.objects.all(), required=False)


class AgendamentoModelForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['horario', 'cliente', 'funcionario']


        error_messages = {
            'horario':{'required':'O horario é um campo obrigatorio'},
            'cliente':{'required':'O cliente é um campo obrigatorio'},
            'funcionario':{'required':'O funcionario é um campo obrigatorio'},
        }