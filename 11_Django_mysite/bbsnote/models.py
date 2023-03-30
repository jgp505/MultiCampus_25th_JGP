from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] {self.subject}' 

class Comment(models.Model):
    # CASCADE : 같이 지워지게 하기? 다른 CLASS에 영향을 같이 받는거 
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.board.id}:{self.board.subject}] {self.content} - {self.author}' 