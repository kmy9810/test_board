from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:id>', views.comment, name='comment'),
    path('comment-delete/<int:id>', views.comment_delete, name='comment-delete')
]
