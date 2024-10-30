from django.db import models

# Create your models here.

class ProdutosServico(models.Model):
    servico = models.ForeignKey('servicos.Servico', verbose_name='Serviço', help_text='Nome do serviço realizado', on_delete= models.PROTECT, related_name='servico')

    produto = models.ForeignKey('produtos.Produto', verbose_name='Produto', help_text='Nome do produto utilizado', on_delete= models.PROTECT, related_name='produto')

    quantidade = models.DecimalField('Quantidade', max_digits= 5, decimal_places=2, help_text='Quantidade utilizada de produto',)

    class Meta:
        verbose_name='Produto utilizado'
        verbose_name_plural = 'Produtos utilizados'

        def __str__(self):
            return f'{self.produto}'


