# tweet/models.py
from django.db import models
from user.models import UserModel


class ProductModel(models.Model):
    class Meta:
        db_table = "product"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # 다른 모델에서 찾조
    categorys = (
        ('자유게시판', '자유게시판'),
        ('익명게시판', '익명게시판'),
    )
    category = models.CharField(choices=categorys, max_length=5)
    title = models.CharField(max_length=20, null=False)
    content = models.CharField(max_length=256, default='')
    created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    heart = models.IntegerField(null=False)
    views_content = models.IntegerField(null=False)


def __str__(self):
    return self.created


