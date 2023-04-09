from django.db import models
from user.models import UserModel
from board.models import ProductModel


class HeartModel(models.Model):
    class Meta:
        db_table = "heart"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)  # 다른 모델에서 찾조
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)  # 다른 모델에서 찾조


def __str__(self):
    return self.product
