from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


# 커스텀  유저
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile", # 필드 제목 
            { # 이 그룹에 포함시킬 필드 목록을 튜플로 나열
                "fields" : ("username", "password", "name", "email", "is_host"), "classes":("wide"),
            },
        ),
        (
            "Permissions",
            {
                "fields":(
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes":("collapse",),# 접어두기 버튼 활성화 
            },
        ),
        (
            "important Dates",
            {
                "fields":("last_login", "date_joined")
            },
        ),
    )
    list_display = ("username","email","name","is_host") # list 보여주기 
    