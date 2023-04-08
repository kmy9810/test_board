from django.forms import ModelForm, TextInput, Textarea, Select
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'content']
        categorys = (
            ('자유게시판', '자유게시판'),
            ('익명게시판', '익명게시판'),
        )
        widgets = {
            'category': Select(choices=categorys),
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'resize: none; height: 50px;',
                'placeholder': 'Title'
            }),
            'content': Textarea(attrs={
                "class": "form-control",
                'style': 'resize: none; height: 100px;',
                'placeholder': 'content'
            }),
        }
