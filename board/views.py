from django.shortcuts import render, redirect
from .forms import ProductForm
from comment.forms import CommentForm
from .models import ProductModel
from comment.models import CommentModel
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/board')
    else:
        return redirect('/sign-in')


def board(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            product_form = ProductForm()
            all_content = ProductModel.objects.all()[:10]
            return render(request, 'board/home.html', {'product_form': product_form, 'content': all_content})


def content_list(request, id):
    all_content = ProductModel.objects.filter(category=id)
    return render(request, 'board/contents.html', {'content': all_content})


def content_detail(request, id):
    content = ProductModel.objects.get(id=id)
    all_comment = CommentModel.objects.filter(product_id=id)
    comment_form = CommentForm()
    return render(request, 'board/show_content.html', {'content': content, 'comment_form': comment_form,
                                                       'comment': all_comment})


def save_content(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            product_form = ProductForm()
            all_content = ProductModel.objects.all()
            return render(request, 'board/save_content.html', {'product_form': product_form, 'content': all_content})
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            user = request.user
            product_form = request.POST
            my_content = ProductModel()
            my_content.author = user
            my_content.category = product_form['category']
            my_content.title = product_form['title']
            my_content.content = product_form['content']
            my_content.views_content = 0
            my_content.heart = 0
            my_content.created = datetime.now()
            my_content.save()
            return redirect('/board')