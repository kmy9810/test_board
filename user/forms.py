from django.forms import ModelForm, TextInput, PasswordInput
from .models import UserModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'style': 'width:100%; margin-bottom:20px;',
                'placeholder': 'Username'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width:100%; margin-bottom:20px;',
                'placeholder': 'Password'
            }),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'style': 'width:100%; margin-bottom:20px;',
                'placeholder': 'Check_password'
            })
        }