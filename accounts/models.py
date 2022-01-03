from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import QuerySet
from django.http import HttpRequest


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", "남성"
        FEMALE = "F", "여성"

    gender = models.CharField('성별', max_length=1, blank=True, choices=GenderChoices.choices)
    avatar = models.ImageField('아바타', blank=True, upload_to="accounts/avatar/%Y/%M/%d",
                                   help_text="100px * 100px 크기의 gif/png/jpg 이미지를 업로드해주세요.")

    class ProviderTypeCodeChoices(models.TextChoices):
        LOCAL = "local", "로컬",
        KAKAO = "kakao", "카카오",

    provider_type_code = models.CharField('프로바이더 타입코드', max_length=20, choices=ProviderTypeCodeChoices.choices,
                                          default=ProviderTypeCodeChoices.LOCAL)
    provider_accounts_id = models.PositiveIntegerField('프로바이더 회원번호', default=0)

    @staticmethod
    def login_with_kakao(request: HttpRequest, provider_accounts_id):
        provider_type_code = User.ProviderTypeCodeChoices.KAKAO
        qs: QuerySet = User.objects.filter(provider_type_code=provider_type_code,
                                           provider_accounts_id=provider_accounts_id)

        if not qs.exists():
            username = provider_type_code + "__" + str(provider_accounts_id)
            name = provider_type_code + "__" + str(provider_accounts_id)
            email = ""
            password = ""
            user: User = User.objects.create_user(username=username, email=email, password=password, first_name=name,
                                                  provider_type_code=provider_type_code,
                                                  provider_accounts_id=provider_accounts_id)
        else:
            user: User = qs.first()

        login(request, user)