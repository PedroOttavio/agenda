from django.views.generic import ListView
from .models import Fornecedor

# Create your views here.

class FornecedoresView(ListView):
    model = Fornecedor
    template_name = 'fornecedores.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FornecedoresView, self).get_queryset()
        if buscar:
            return qs.filter( nome__icontains=buscar)

        return qs

