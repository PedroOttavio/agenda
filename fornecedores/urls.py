from django.urls import path

from .views import FornecedoresView, FornecedorAddView

urlpatterns = [
    path('fornecedores', FornecedoresView.as_view(), name='fornecedores'),
    path('fornecedor/adicionar/', FornecedorAddView.as_view(), name='fornecedor_adicionar'),
    path('<int:pk>/fornecedor/editar/', FornecedorAddView.as_view(), name='fornecedor_editar'),
]