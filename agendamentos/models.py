from django.db import models

from clientes.models import Cliente


# Create your models here.

class Agendamento(models.Model):
    horario = models.DateTimeField('Horário', help_text= 'Data e hora do atendimento')
    cliente = models.ForeignKey('clientes.Cliente', verbose_name='Cliente', help_text='Nome do cliente', on_delete=models.PROTECT)

    funcionario = models.ForeignKey('funcionarios.Funcionario', verbose_name='Funcionario', help_text='Nome do Funcionario', on_delete= models.PROTECT)


    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'

    def __str__(self):
        return f'Cliente:{self.cliente}'
