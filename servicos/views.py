from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from servicos.forms import ServicoModelForm
from servicos.models import Servico


# Create your views here.

class ServicosView(ListView):
    model = Servico
    template_name = 'servicos.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ServicosView, self).get_queryset()


        if buscar:
            qs = qs.filter(Q(nome__icontains=buscar)|Q(descricao__icontains=buscar))


        if qs.count() > 0:
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem serviços cadastrados!')

class ServicosAddView(SuccessMessageMixin, CreateView):
    model = Servico
    form_class = ServicoModelForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Serviço cadastrado com sucesso!'


class ServicosUpdateView(SuccessMessageMixin, UpdateView):
    model = Servico
    form_class = ServicoModelForm
    template_name = 'servico_form.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Serviço alterado com sucesso!'

class ServicosDeleteView(SuccessMessageMixin, DeleteView):
    model = Servico
    template_name = 'servico_apagar.html'
    success_url = reverse_lazy('servicos')
    success_message = 'Serviço alterado com sucesso'


