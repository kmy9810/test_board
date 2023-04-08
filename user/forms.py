from django.forms import ModelForm, TextInput, PasswordInput
from .models import UserModel


# class UserForm(forms.Form):
#     username = forms.CharField(max_length=50, label='아이디')
#     password = forms.CharField( max_length=20, label='비밀번호', widget=forms.PasswordInput)
#     password2 = forms.CharField(max_length=20, label='비밀번호확인', widget=forms.PasswordInput)

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
            })
        }