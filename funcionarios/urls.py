from django.urls import path
from .views import FuncionariosView, FuncionarioAddView, FuncionarioUpdateView, FuncionarioDeleteView

urlpatterns = [
    path('funcionarios', FuncionariosView.as_view(), name='funcionarios'),
    path('cliente/adicionar/', FuncionarioAddView.as_view(), name='funcionario_adicionar'),
    path('<int:pk>/funcionario/editar/', FuncionarioUpdateView.as_view(), name='funcionario_editar'),
    path('<int:pk>/funcionario/apagar/', FuncionarioDeleteView.as_view(), name='funcionario_apagar'),

]