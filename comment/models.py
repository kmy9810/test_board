from django.db import models
from user.models import UserModel
from board.models import ProductModel


class CommentModel(models.Model):
    class Meta:
        db_table = "comment"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # 다른 모델에서 찾조
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)  # 다른 모델에서 찾조
    comment = models.CharField(max_length=256, default='')
    created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    heart = models.IntegerField(null=False)


def __str__(self):
    return self.created
