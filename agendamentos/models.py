from django.db import models
from django.db.models.functions import Upper



from clientes.models import Cliente
from ordemservicos.models import OrdemServicos

from django.forms import forms
from funcionarios.models import Funcionario


# Create your models here.




class Agendamento(models.Model):
    horario = models.DateTimeField('Horário', help_text= 'Data e hora do atendimento')
    cliente = models.ForeignKey('clientes.Cliente', verbose_name='Cliente', help_text='Nome do cliente', on_delete=models.PROTECT)
    funcionario = models.ForeignKey('funcionarios.Funcionario', verbose_name='Funcionario', help_text='Nome do Funcionario', on_delete= models.PROTECT)
    servico = models.ManyToManyField('servicos.Servico', verbose_name='Serviço', through='ordemservicos.OrdemServicos')

    valor = models.DecimalField('Valor total', max_digits=6, decimal_places=2, default=0.00)
    status = models.CharField('Status', max_length=1, help_text='Status do agendamento', default='A')


    @property
    def servicos(self):
        return OrdemServicos.objects.filter(agendamento=self)

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering = [Upper('-horario')]

    def __str__(self):
        return f'Cliente:{self.cliente}'

    class AgendamentoListForm(forms.Form):
        cliente = forms.ModelChoiceField(label='Cliente', queryset=Cliente.objects.all(), required=False)
        funcionario = forms.ModelChoiceField(label='Funcionário', queryset=Funcionario.objects.all(), required=False)

    class AgendamentoModelForm(forms.ModelForm):
        class Meta:
            model = Agendamento
            fields = ['horario', 'cliente', 'funcionario']

            error_messages = {
                'horario': {'required': 'O horário é um campo obrigatório'},
                'cliente': {'required': 'O cliente é um campo obrigatório'},
                'funcionario': {'required': 'O funcionário é um campo obrigatório'},
            }


