from django.db import models

from produtosservico.models import ProdutosServico


# Create your models here.


class Servico(models.Model):
    nome = models.CharField('Nome',max_length=100, help_text='Nome completo do serviço', unique=True)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2, help_text='Preço do serviço')
    descricao = models.TextField('Descrição', max_length=300, help_text='Descrição e observações do serviço')
    produto = models.ManyToManyField('produtos.Produto', through='produtosservico.ProdutosServico')

    @property
    def produtos(self):
        return ProdutosServico.objects.filter(servico=self)


    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome