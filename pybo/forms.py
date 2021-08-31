from django import forms
from pybo.models import Article, Answer


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 사용할 모델
        fields = ['subject', 'content', 'category']  # QuestionForm에서 사용할 Question 모델의 속성


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }