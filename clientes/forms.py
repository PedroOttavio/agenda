from django import forms


from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereco', 'fone','email','foto']

        error_messages = {
            'nome': {'required': 'O nome do cliente é um campo obrigatorio'},
            'endereco': {'required': 'O endereço do cliente é um campo obrigatorio'},
            'fone': {'required': 'O fone do cliente é um campo obrigatorio'},
            'email': {'required': 'O e-mail do cliente é um campo obrigatorio',
                'invalid':'Formato invalido para o e-mail. Exemplo de formato valido: fulano@dominio.com',
                'unique':'E-mail já cadastrado'
            }
        }


