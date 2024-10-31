# Generated by Django 5.1.2 on 2024-10-30 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('produtosservico', '0002_alter_produtosservico_produto_and_more'),
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='produto',
            field=models.ManyToManyField(through='produtosservico.ProdutosServico', to='produtos.produto'),
        ),
    ]
