from django.db import models

# models.Model을 상송하는 새로운 클래스 Board를 정의. 데이터 베이스 테이블을 나타냄
class Board(models.Model) : # 게시글
    # 문자열필드(CharField) 형태로 최대 길이 200 자로 제한
    subject = models.CharField(max_length=200)
    # 텍스트 필드
    content = models.TextField()
    #날짜/시간 필드 / 객체가 처음 생성될 때 자동으로 현재 날짜/시간으로 설정, 생성시 딱 한 번 
    create_date = models.DateTimeField(auto_now_add=True) 
    #날짜/시간 필드 / 객체가 저장될 때마다 현재 날짜/시간으로 설정
    update_date = models.DateTimeField(auto_now=True) 
    
    def __str__(self) :
        # Board를 불러올 때, [id][제목] 형태로 객체를 출력
        return f'[{self.id}] {self.subject}'
    
class Comment(models.Model) : # 댓력
    # 외래 키 필드, Board 모델을 기반으로 함
    # on_delete 옵션은 Board 객체가 삭제될 때 관련된 Comment 객체도 함께 사라지도록 지정
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    # 텍스트 필드
    content = models.TextField()
    # 날짜/시간 필드
    create_date = models.DateTimeField()
    
