from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin) : 
    # 관리자 페이지에서 검색 가능한 필드를 제목(subject)과 내용(content) 검색 가능하게 함
    search_fields = ['subject', 'content'] # 검색 기능 추가
# 관리자 페이지에 Board모델을 등록하고 이 모델은 위의 클래스의 정의된 방식으로 표시
admin.site.register(Board, BoardAdmin)