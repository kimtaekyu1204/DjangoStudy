from django.db import models
# Describe the structure (schema) of the data (shape of data)
class House(models.Model):
    """ Model Definition for Houses """
    name = models.CharField(max_length=140) # max_length는 필수요소임 
    price = models.PositiveIntegerField(help_text="price per night")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(
        default=False,
        verbose_name="Pets Allowed?", # 표시될 이름 변경 
        help_text="Does this house allow pets", # 간단한 설명 
        )
    owner = models.ForeignKey("users.User",on_delete=models.CASCADE, null=True,blank=True) # on_delete는 필수요소 -> 연결된 요소가 삭제될때 어떻게 할지 결정 
    # models.SET_NULL -> 삭제하지말고 유지
    # models.CASCADE -> 같이 삭제  

    # 객체를 문자열로 표현할때 호출되는 함수 
    def __str__(self):
        return self.name

