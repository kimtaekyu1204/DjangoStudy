from django.db import models
# Describe the structure (schema) of the data (shape of data)
class House(models.Model):
    """ Model Definition for Houses """
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField(help_text="price per night")
    description = models.TextField()
    address = models.CharField(max_length=140)
    pet_allowed = models.BooleanField(
        default=False,
        verbose_name="Pets Allowed?", # 표시될 이름 변경 
        help_text="Does this house allow pets", # 간단한 설명 
        )

    # 객체를 문자열로 표현할때 호출되는 함수 
    def __str__(self):
        return self.name

