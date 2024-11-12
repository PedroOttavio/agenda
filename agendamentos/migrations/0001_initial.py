# Generated by Django 5.1.2 on 2024-11-06 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField(help_text='Data e hora do atendimento', verbose_name='Horário')),
                ('cliente', models.ForeignKey(help_text='Nome do cliente', on_delete=django.db.models.deletion.PROTECT, to='clientes.cliente', verbose_name='Cliente')),
                ('funcionario', models.ForeignKey(help_text='Nome do Funcionario', on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario', verbose_name='Funcionario')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]