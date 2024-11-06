# Generated by Django 5.1.2 on 2024-11-06 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdutosServico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.DecimalField(decimal_places=2, help_text='Quantidade utilizada de produto', max_digits=5, verbose_name='Quantidade')),
                ('produto', models.ForeignKey(help_text='Nome do produto utilizado', on_delete=django.db.models.deletion.PROTECT, related_name='produto', to='produtos.produto', verbose_name='Produto')),
            ],
            options={
                'verbose_name': 'Produto utilizado',
                'verbose_name_plural': 'Produtos utilizados',
            },
        ),
    ]
