from django.contrib import admin
from .models import MainList, SubList


@admin.register(MainList)
class AdminMainList(admin.ModelAdmin):
    pass


@admin.register(SubList)
class AdminSubList(admin.ModelAdmin):
    pass
