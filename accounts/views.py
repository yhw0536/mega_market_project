from django.contrib import messages
from django.contrib.auth.views import logout_then_login, LoginView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from .forms import SignupForm

signin = LoginView.as_view(template_name="accounts/signin.html")



def signout(request: HttpRequest):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            signed_user = form.save()
            auth_login(request, signed_user)
            messages.success(request, "회원가입을 환영합니다.")
            # signed_user.send_welcome_email()
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })