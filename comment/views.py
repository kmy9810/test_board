from django.shortcuts import render, redirect
from .models import CommentModel
from board.models import ProductModel
from datetime import datetime


def comment(request, id):
    if request.method == 'POST':
        my_comment = CommentModel()
        my_comment.comment = request.POST.get('comment', '')
        my_comment.author = request.user
        my_comment.product = ProductModel.objects.get(id=id)
        my_comment.created = datetime.now()
        my_comment.heart = 0
        my_comment.save()
        return redirect(f'/posting/{id}')


def comment_delete(request, id):
    delete_comment = CommentModel.objects.get(id=id)
    delete_comment.delete()
    return redirect(f'/posting/{delete_comment.product.id}')