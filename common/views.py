from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #cleaned_data.get : form에서 특정 값을 얻고 싶을 때 사용 
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  #authenticate의 login함수. 자동 로그인하게 해줌
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def resetpw(request):
    try:
        send_success=send_mail(
        'pybo 비밀번호가 재생성되었습니다.',
        '다음 비밀번호로 로그인해주세요 :\n qwer1234!@',
        'dlatmddnjs20@gmail.com',
        ['dlatmddnjs20@naver.com'],
        fail_silently=False,
        )
    except Exception:
        send_success=0
    context = {'statuscode': send_success}

    return render(request, 'common/resetpw.html', context)


def changepw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
        #원래는 form을 전달하면 좋지만 customizing을 위해서 전달하지 않았음
    return render(request, 'common/changepw.html')
