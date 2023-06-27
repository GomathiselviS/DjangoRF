from django.urls import path
from .views import Quiz, RandomSlogan, QuizSlogan, GetRandomSlogan, SloganandBrandbyid
from rest_framework.urlpatterns import format_suffix_patterns


app_name = "quiz"

urlpatterns = format_suffix_patterns([
    path("", Quiz.as_view(), name="quiz"),
    path("r/<str:topic>/", RandomSlogan.as_view(), name="random"),
    path("q/<str:topic>/", QuizSlogan.as_view(), name="slogans"),
    path("ask/<str:topic>/", GetRandomSlogan.as_view(), name="slogan-detail"),
    path("answer/<int:num>/", SloganandBrandbyid.as_view(), name="slogan-brand"),

])
