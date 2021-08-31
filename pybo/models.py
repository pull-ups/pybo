from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = {
        ('질문','질문게시판'), #오른쪽에 있는 것이 화면에 보인다.
        ('정보', '정보게시판'),
        ('인사', '인사게시판')
    }

    category = models.TextField(default='', choices=CATEGORY_CHOICES, null=False)
    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE,  null=True)
    content = models.TextField()
    create_date = models.DateTimeField()