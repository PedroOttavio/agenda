from lib2to3.fixes.fix_input import context

from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages #resolve o problema do info
from django.views.generic.base import TemplateResponseMixin

from .models import Agendamento
from .forms import AgendamentoListForm, AgendamentoModelForm, AgendamentosServicoInLine


# Create your views here.


class AgendamentosView(ListView):
    model = Agendamento
    template_name = 'agendamentos.html'

    def get_context_data(self, **kwargs):
        context = super(AgendamentosView, self).get_context_data(**kwargs)
        if self.request.GET:
            form = AgendamentoListForm(self.request.GET)
        else:
            form = AgendamentoListForm()
        context['form'] = form
        return context

    def get_queryset(self):
        qs = super(AgendamentosView, self).get_queryset()
        if self.request.GET:
            form = AgendamentoListForm(self.request.GET)
            if form.is_valid():
                cliente = form.cleaned_data.get('cliente')
                funcionario = form.cleaned_data.get('funcionario')
                if cliente:
                    qs = qs.filter(cliente=cliente)
                if funcionario:
                    qs = qs.filter(funcionario=funcionario)
        if qs.count() > 0:
            print(qs)
            paginator = Paginator(qs, 1)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem agendamentos cadastrados!')

class AgendamentoAddView(SuccessMessageMixin, CreateView):
    model = Agendamento
    form_class = AgendamentoModelForm
    template_name = 'agendamento_form.html'
    success_url = reverse_lazy('agendamentos')
    success_message = 'Agendamento cadastrado com sucesso!'

class AgendamentoUpdateView(SuccessMessageMixin, UpdateView):
    model = Agendamento
    form_class = AgendamentoModelForm
    template_name = 'agendamento_form.html'
    success_url = reverse_lazy('agendamentos')
    success_message = 'Agendamento alterado com sucesso!'

class AgendamentoDeleteView(SuccessMessageMixin, DeleteView):
    model = Agendamento
    template_name = 'agendamento_apagar.html'
    success_url = reverse_lazy('agendamentos')
    success_message = 'Agendamento apagado com sucesso!'


class AgendamentoInLineEditView(TemplateResponseMixin, View):
    template_name = 'agendamento_form_inLine.html'

    def get_formset(self, data=None):
        return AgendamentosServicoInLine(instance=self.agendamento, data=data)

    def dispatch(self, request, pk):
        self.agendamento = get_object_or_404(Agendamento, id=pk)
        return super().dispatch(request, pk)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'agendamento': self.agendamento, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('agendamentos')
        return self.render_to_response({'agendamento': self.agendamento, 'formset':formset})
