from django.forms import ModelForm, TextInput, Textarea, Select
from .models import ProductModel


class ProductForm(ModelForm):
    class Meta:
        model = ProductModel
        fields = ['category', 'title', 'imgfile', 'content']  # 모델에 없는 필드 사용시 오류.
        labels = {
            'category': '카테고리',
            'title': '제목',
            'imgfile': '이미지',
            'content': '내용'
        }
