from django import forms


from .models import Funcionario

class FuncionarioModelForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['nome', 'funcao', 'fone','email','data_admissao', 'foto']

        error_messages = {
            'nome': {'required': 'O nome do funcionario é um campo obrigatorio'},
            'funcao': {'required': 'A funcao do funcionario é um campo obrigatorio'},
            'fone': {'required': 'O fone do funcionario é um campo obrigatorio'},
            'email': {'required': 'O e-mail do funcionario é um campo obrigatorio',
                'invalid':'Formato invalido para o e-mail. Exemplo de formato valido: fulano@dominio.com',
                'unique':'E-mail já cadastrado'
            },
            'data_admissao':{'required': ' A data de admissao é um campo obrigatório'},
        }


