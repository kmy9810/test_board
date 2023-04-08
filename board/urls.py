from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
    path('board/', views.board, name='board'),
    path('board/<str:id>', views.content_list, name='show_content'),  # 카테고리별 목차
    path('posting/<int:id>', views.content_detail, name='content_detail'),
    path('posting', views.save_content, name='save_content'),
    # path('erp/delete-inventory/<int:id>', views.delete_inventory, name='delete-inventory'),
]
