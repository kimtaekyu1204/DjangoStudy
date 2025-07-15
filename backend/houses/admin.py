from django.contrib import admin
from .models import House 
# Register your models here.

@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # admin column 변경 
    list_display = (
        # column은 model의 property 이여야함 
        "name",
        "price",
        "address",
        "pet_allowed",
    )
    list_filter = (
        "price",
        "pet_allowed"
    )
    search_fields = ("address",)
    fields = ("name", "address", ("price", "pet_allowed"),)