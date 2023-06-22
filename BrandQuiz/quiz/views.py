from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Slogan
from .serializers import QuizSerializer, RandomSloganSerializer, SloganSerializer
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomSlogan(APIView):
    def get(self, request, format=None, **kwargs):
        slogan = Slogan.objects.filter(quiz__title=kwargs["topic"]).order_by("?")[:1]
        serializer = RandomSloganSerializer(slogan, many=True)
        return Response(serializer.data)


class QuizSlogan(APIView):
    def get(self, request, format=None, **kwargs):
        quiz = Slogan.objects.filter(quiz__title=kwargs["topic"])
        serializer = SloganSerializer(quiz, many=True)
        return Response(serializer.data)
