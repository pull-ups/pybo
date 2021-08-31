from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Answer
from .forms import ArticleForm, AnswerForm
from django.core.paginator import Paginator  
from django.db.models import Q

from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):

    page = request.GET.get('page', '1')

    article_list = Article.objects.order_by('-create_date')

    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    categories=['질문게시판', '정보게시판', '인사게시판']
    context = {'article_list': page_obj, 'categories' : categories}
    
    return render(request, 'pybo/total_article.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    print(article)
    context = {'article': article}
    return render(request, 'pybo/question_detail.html', context)


def category_index(request, selected_category):

    page = request.GET.get('page', '1')
    article_list = Article.objects.order_by('-create_date')
    
    article_list = article_list.filter(Q(category=selected_category[:2]))
    
    paginator = Paginator(article_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    categories=['질문게시판', '정보게시판', '인사게시판']

    context={'article_list': page_obj, 
             'selected_category' : selected_category, 
             'categories' : categories}


    return render(request, 'pybo/selected_article.html', context)

@login_required(login_url='common:login')
def answer_create(request, article_id):

    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.article = article
            answer.save()
            answer.author = request.user  # author 속성에 로그인 계정 저장
            return redirect('pybo:detail', article_id=article.id)
    else:
        form = AnswerForm()
    context = {'article': article, 'form': form}
    return render(request, 'pybo/question_detail.html', context)  

@login_required(login_url='common:login')
def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.create_date = timezone.now()

            article.save()
            article.author = request.user  # author 속성에 로그인 계정 저장
            return redirect('pybo:index')
    else:
        form = Article()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)