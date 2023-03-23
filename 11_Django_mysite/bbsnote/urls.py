from django.urls import path
from . import views

# 앱 이름을 bbsnote로 지정, URL 패턴의 기반(결국, mysite/bbsnote 가 생성되면서 application으로 인식됨)
app_name='bbsnote'

urlpatterns = [
    path('',views.index,name='index'), # URL 패턴에 빈 문자열인 경우(즉,/bbsnote), views.index 함수를 호출
    path('<int:board_id>/',views.detail,name="detail"), # board_id와 일치한 정수형 변수인 경우 views.detail 함수를 호출(/bbsnote/1)
    path('comment/create/<int:board_id>/', views.comment_create, name='comment_create'), # comment/create 이 후 board_id와 일치한 정수형 변수인 경우, views.comment_create 함수 호출
]