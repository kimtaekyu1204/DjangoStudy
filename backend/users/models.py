from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # first_name과 last_name 사용 안하기 위함 
    first_name = models.CharField(max_length=150, editable=False) # editable -> 폼/관리자 페이지에서 숨기고 싶을때 사용 
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="anonymous")
    is_host = models.BooleanField(default=False)