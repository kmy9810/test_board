from django.forms import ModelForm, TextInput, Textarea
from .models import CommentModel


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={
                "class": "form-control",
                'style': 'resize: none; height: 100px;',
                'placeholder': 'content'
            }),
        }
