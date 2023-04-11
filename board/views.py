from django.shortcuts import render, redirect
from .forms import ProductForm
from comment.forms import CommentForm
from .models import ProductModel
from heart.models import HeartModel
from comment.models import CommentModel
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model  # 사용자가 데이터베이스 안에 있는지 검사하는 함수
# Create your views here.


def home(request):
    user = request.user.is_authenticated
    if user:
        all_content = ProductModel.objects.all().order_by('-created')
        page = request.GET.get('page')

        paginator = Paginator(all_content, 1)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:  # page 숫자가 없을 시
            page = 1
            page_obj = paginator.page(page)
        except EmptyPage:   # page 숫자가 너무 클 시 마지막 페이지를 보여줌
            page = paginator.num_pages
            page_obj = paginator.page(page)

        # 앞으로 2개 뒤로 2개 총 5개가 기본적으로 보이는 pagination
        left_index = (int(page) - 2)
        if left_index < 1:
            left_index = 1

        right_index = (int(page) + 2)
        if right_index > paginator.num_pages:
            right_index = paginator.num_pages

        custom_range = range(left_index, right_index+1)
        return render(request, 'board/home.html', {'content': all_content, 'page_obj': page_obj,
                                                   'paginator': paginator, 'custom_range': custom_range})
    else:
        return redirect('/sign-in')


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
            return redirect(f'/posting/{my_content.id}')


def heart(request, id):
    user = request.user
    # if not HeartModel.objects.get(author_id=user):
    #     delete_heart = HeartModel.objects.get(author_id=user.id)
    #     delete_heart.delete()
    # else:
    my_heart = HeartModel()
    my_heart.author = request.user
    my_heart.product = ProductModel.objects.get(id=id)
    return redirect(f'/posting/{id}')