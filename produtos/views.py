from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator

from .models import Produto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ProdutoModelForm
from produtos.models import Produto


# Create your views here.

class ProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ProdutosView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem produtos cadastrados!')

class ProdutoAddView(SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')
    sucess_message = 'Produto cadastrado com sucesso!'

class ProdutoUpdateView(SuccessMessageMixin, UpdateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')
    sucess_message = 'Produto alterado com sucesso!'

class ProdutoDeleteView(SuccessMessageMixin, DeleteView):
    model = Produto
    template_name = 'produto_apagar.html'
    success_url = reverse_lazy('produtos')
    sucess_message = 'Produto apagado com sucesso!'


