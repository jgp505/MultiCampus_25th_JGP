from django.urls import path
from . import views

app_name = 'bbsnote'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('comment/create/<int:board_id>/', views.comment_create, name='comment_create'),
    path('board/create/', views.board_create, name='board_create'),
    path('board/modify/<int:board_id>/', views.board_modify, name='board_modify'),
    path('board/delete/<int:board_id>/',views.board_delete,name='board_delete'),
    path('comment/modify/<int:comment_id>/',views.comment_modify,name='comment_modify'),
    path('comment/delete/<int:comment_id>/',views.comment_delete,name='comment_delete'),
]