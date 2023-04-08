from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
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
            all_content = Product.objects.all()[:10]
            return render(request, 'board/home.html', {'product_form': product_form, 'content': all_content})


def content_list(request, id):
    all_content = Product.objects.filter(category=id)
    print(all_content)
    return render(request, 'board/contents.html', {'content': all_content})


def content_detail(request, id):
    content = Product.objects.get(id=id)
    return render(request, 'board/show_content.html', {'content': content})


def save_content(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            product_form = ProductForm()
            all_content = Product.objects.all()
            return render(request, 'board/save_content.html', {'product_form': product_form, 'content': all_content})
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            user = request.user
            product_form = request.POST
            my_content = Product()
            my_content.author = user
            my_content.category = product_form['category']
            my_content.title = product_form['title']
            my_content.content = product_form['content']
            my_content.views_content = 0
            my_content.heart = 0
            my_content.created = datetime.now()
            my_content.save()
            return redirect('/board')