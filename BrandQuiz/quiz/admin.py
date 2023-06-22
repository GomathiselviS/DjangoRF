from django.contrib import admin
from . import models


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
    ]


class BrandInlineModel(admin.TabularInline):
    model = models.Brand
    fields = ["brand_text", "is_right"]


@admin.register(models.Slogan)
class SloganAdmin(admin.ModelAdmin):
    fields = [
        "question",
        "quiz",
    ]
    list_display = [
        "question",
        "quiz",
    ]
    inlines = [
        BrandInlineModel,
    ]


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["brand_text", "is_right", "slogan"]
