from django import forms


from .models import Produto

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do cliente é um campo obrigatorio', 'unique':'Produto já cadastrado'},
            'preco':{'required': 'O preço do produto é um campo obrigatorio'},
            'quantidade':{'required':'A quantidade em estoque do produto é um campo obrigatorio'},

        }


