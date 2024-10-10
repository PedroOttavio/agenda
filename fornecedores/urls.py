from django.urls import path

from .views import FornecedoresView


urlpatterns = [
    path('fornecedores', FornecedoresView.as_view(), name='fornecedores'),
]