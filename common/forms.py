from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

# UserForm은 django.contrib.auth.forms 모듈의 UserCreationForm 클래스를 상속하여 만들었다
# UserCreationfORM : username, pw1, pw2만 갖고 있음
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
'''
class ChangePWForm():
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")
'''
