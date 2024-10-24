from django.shortcuts import render

# Create your views here.

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from pyexpat.errors import messages
from django.contrib.messages.context_processors import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Funcionario

from .forms import FuncionarioModelForm
from .models import Funcionario

# Create your views here.

# class FuncionariosView(ListView):
#     model = Funcionario
#     template_name = 'funcionarios.html'
#
#     def get_queryset(self):
#         buscar = self.request.GET.get('buscar')
#         qs = super(FuncionariosView, self).get_queryset()
#
#
#         if buscar:
#             qs = qs.filter( nome__icontains=buscar)
#
#         if qs.count() > 0:
#             paginator = Paginator(qs, 5)
#             listagem = paginator.get_page(self.request.GET.get('page'))
#             return listagem
#         else:
#             return messages.info(self.request, 'Não existem funcionarios cadastrados!')




class FuncionariosView(ListView):
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super().get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        # Handle empty queryset with messages
        if qs.count() == 0:
            messages.info(self.request, 'Não existem funcionarios cadastrados!')

        # Paginate the queryset regardless
        paginator = Paginator(qs, 5)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem


class FuncionarioAddView(SuccessMessageMixin, CreateView):
    model = Funcionario
    form_class = FuncionarioModelForm
    template_name = 'Funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario cadastrado com sucesso!'

class FuncionarioUpdateView(SuccessMessageMixin, UpdateView):
    model = Funcionario
    form_class = FuncionarioModelForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    sucess_message = 'Funcionario atualizado com sucesso!'

class FuncionarioDeleteView(SuccessMessageMixin, DeleteView):
    model = Funcionario
    form_class = FuncionarioModelForm
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')
    sucess_message = 'Funcionario excluído com sucesso!'