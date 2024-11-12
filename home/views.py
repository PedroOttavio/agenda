from django.views.generic import TemplateView

from agendamentos.models import Agendamento
from clientes.models import Cliente
from fornecedores.models import Fornecedor
from funcionarios.models import Funcionario
from produtos.models import Produto
from servicos.models import Servico


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        context['qtd_clientes'] = Cliente.objects.count()
        context['qtd_funcionarios'] = Funcionario.objects.count()
        context['qtd_fornecedores'] = Fornecedor.objects.count()
        context['qtd_servicos'] = Servico.objects.count()
        context['qtd_produtos'] = Produto.objects.count()
        context['qtd_agendamentos'] = Agendamento.objects.count()
        return context
