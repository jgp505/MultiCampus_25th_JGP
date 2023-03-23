from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone

# Create your views here.
def index(request): # :는 붙여야 한다!   
    # Board 모델의 객체 목록을 가져옴. 이후, 생성 날짜의 역순으로 정
    board_list = Board.objects.order_by('-create_date')
    # 템플릿에 전달하기 위한 수단
    context = {'board_list':board_list}
    # HTTP 응답이 오면, bbsnote/ 이후에 url를 형성 시켜준다. 그리고, context 객체를 반환
    return render(request, 'bbsnote/board_list.html', context)
    #return HttpResponse("bbstnote에 오신것을 환영합니다!")
    
def detail(request, board_id):
    board = Board.objects.get(id=board_id) # mysql 에서 select * from bbsnote_board where id=board_id 와 같은 개념
    context = {'board': board}
    return render(request, 'bbsnote/board_detail.html',context)
    
def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    comment = Comment(board=board,content=request.POST.get('content'), create_date=timezone.now())
    comment.save()
    #board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('bbsnote:detail',board_id=board.id)