# Generated by Django 5.1.2 on 2024-11-06 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agendamentos', '0001_initial'),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdemServicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situacao', models.CharField(choices=[('A', 'Agendado'), ('R', 'Realizado'), ('C', 'Cancelado')], default='A', max_length=1, verbose_name='Situação')),
                ('observacoes', models.TextField(blank=True, max_length=300, null=True, verbose_name='Observações')),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, help_text='Preço do serviço', max_digits=5, verbose_name='Preço')),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agendamento', to='agendamentos.agendamento', verbose_name='Agendamento')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funcionario', to='funcionarios.funcionario', verbose_name='Funcionario')),
            ],
            options={
                'verbose_name': 'Serviço realizado',
                'verbose_name_plural': 'Serviços realizados',
            },
        ),
    ]
