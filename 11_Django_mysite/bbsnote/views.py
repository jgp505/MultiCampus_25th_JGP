from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone
from .forms import BoardForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    # 입력인자
    page = request.GET.get('page', 1)
    # 조회
    board_list = Board.objects.order_by('-create_date')
    # 페이징처리
    paginator = Paginator(board_list, 3)
    page_obj = paginator.get_page(page)
    context = {'board_list': page_obj}
    # return HttpResponse("bbsnote에 오신 것을 환영합니다")
    return render(request, 'bbsnote/board_list.html', context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)    
    context = {'board': board}
    return render(request, 'bbsnote/board_detail.html', context)

# login을 필수 사항으로 넣음
@login_required(login_url='common:login')
def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    # comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now())
    # comment.save()
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now(), author=request.user)
    return redirect('bbsnote:detail', board_id=board_id)


@login_required(login_url='common:login')
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            # board.create_date = timezone.now()
            board.author = request.user
            board.save()
            return redirect('index')
    else:
        form = BoardForm()
    return render(request, 'bbsnote/board_form.html', {'form':form})

@login_required(login_url='common:login')
def board_modify(request, board_id):
    # 404 페이지 에러시 (pk = primary key 줄임말)
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.author :
        messages.error(request, '수정권한이 없습니다.')
        # 오류 발생 시, /bbsnote/detail로 돌아가기
        return redirect('bbsnote:detail', board_id=board.id)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            board.update_date = timezone.now()
            board.save()
            return redirect('bbsnote:detail', board_id=board.id)
    else:
        form = BoardForm(instance=board) # 기존에 있던 board 내용을 불러오는 것
    context = {'form':form}
    return render(request, 'bbsnote/board_form.html',context)

@login_required(login_url='common:login')
def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    if request.user != board.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('bbsnote:detail', board_id=board.id)
    board.delete()
    return redirect('bbsnote:index')

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author :
        messages.error(request, '수정권한이 없습니다.')
        return redirect('bbsnote:detail', board_id=comment.board.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('bbsnote:detail', board_id=comment.board.id)
    else :
        form = CommentForm(instance=comment) # 기존에 있던 board 내용을 불러오는 것
    context = {'comment':comment,'form':form}
    return render(request, 'bbsnote/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다')
        return redirect('bbsnote:detail', board_id=comment.board.id)
    comment.delete()
    return redirect('bbsnote:detail', board_id=comment.board.id)