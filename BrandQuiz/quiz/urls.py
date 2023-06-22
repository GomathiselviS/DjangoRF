from django.urls import path
from .views import Quiz, RandomSlogan, QuizSlogan

app_name = "quiz"

urlpatterns = [
    path("", Quiz.as_view(), name="quiz"),
    path("r/<str:topic>/", RandomSlogan.as_view(), name="random"),
    path("q/<str:topic>/", QuizSlogan.as_view(), name="slogans"),
]
