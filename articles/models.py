from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set => Article과 Comment가 foreign key로 연결되면서 자동생성

class Comment(models.Model):
    content = models.TextField()
    # article이라는 클래스와 연결해주는 id 컬럼을 하나 더 지정
    # foreign key: 다대일 (게시물-댓글) 구조일 때 사용
    # on delete: 게시물 자체가 지워졌을 때, 그 영향이 폭포처럼 아래로 내려간다는 것 > 게시물 삭제시 댓글도 다 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article.id => Article과 Comment가 foreign key로 연결되면서 자동생성