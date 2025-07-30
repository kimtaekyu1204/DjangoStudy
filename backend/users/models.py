from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male") # (Value, Label) -> (DB의 값, 관리자 페이지에서 볼 label)
        FEMALE = ("female","Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr","Korean")
        EN = ("en","English")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    # first_name과 last_name 사용 안하기 위함 
    first_name = models.CharField(max_length=150, editable=False) # editable -> 폼/관리자 페이지에서 숨기고 싶을때 사용 
    last_name = models.CharField(max_length=150, editable=False)

    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True) # 아바타 사진 
    name = models.CharField(max_length=150, default="anonymous")
    is_host = models.BooleanField(default=False)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices, null=True, blank=True) # class로 choices를 만들었음 
    language = models.CharField(max_length=2,choices=LanguageChoices.choices , null=True, blank=True)
    currency = models.CharField(max_length=100, choices=CurrencyChoices.choices, null=True, blank=True)