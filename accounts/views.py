from django.contrib import messages
from django.contrib.auth.views import logout_then_login, LoginView
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet

from .forms import SignupForm, FindUsernameForm
from .decorators import logout_required
from django.urls import reverse
from lazy_string import LazyString

from .models import User


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = "accounts/signin.html"
    next_page = "/"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.success_message = LazyString(
            lambda: f'{self.request.user.last_name}{self.request.user.first_name}님 환영합니다.')

    def get_initial(self):
        initial = self.initial.copy()
        initial['username'] = self.request.GET.get('username', None)

        return initial

@logout_required
def signin(request: HttpRequest):
    return MyLoginView.as_view()(request)


def signout(request: HttpRequest):
    messages.success(request, "로그아웃 되었습니다.")
    return logout_then_login(request)


@logout_required
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


def find_username(request: HttpRequest):
    if request.method == 'POST':
        form = FindUsernameForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']

            qs: QuerySet = User.objects.filter(email=email, first_name=first_name)

            if not qs.exists():
                messages.warning(request, "일치하는 회원이 존재하지 않습니다.")
            else:
                user: User = qs.first()
                messages.success(request, f"해당회원의 username은 {user.username} 입니다.")
                return redirect(reverse("accounts:signin") + '?username=' + user.username)
    else:
        form = FindUsernameForm()

    return render(request, 'accounts/find_username.html', {
        'form': form,
    })
