from django.urls import path

from .views import ServicosView, ServicosAddView, ServicosUpdateView, ServicosDeleteView, ServicoInLineEditView

urlpatterns = [
    path('servicos/', ServicosView.as_view(), name='servicos'),
    path('servico/adicionar', ServicosAddView.as_view(), name='servico_adicionar'),
    path('<int:pk>/servico/editar', ServicosUpdateView.as_view(), name='servico_editar'),
    path('<int:pk>/servico/apagar', ServicosDeleteView.as_view(), name='servico_apagar'),
    path('<int:pk>/servico/inLine', ServicoInLineEditView.as_view(), name='servico_inline'),
]