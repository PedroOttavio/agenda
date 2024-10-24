from django.urls import path

from .views import ProdutosView, ProdutoAddView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('produtos', ProdutosView.as_view(), name='produtos'),
    path('produto/adicionar/',ProdutoAddView.as_view(), name='produto_adicionar'),
    path('<int:pk>/produto/editar/',ProdutoUpdateView.as_view(), name='produto_editar'),
    path('<int:pk>/produto/apagar/',ProdutoDeleteView.as_view(), name='produto_apagar'),
]