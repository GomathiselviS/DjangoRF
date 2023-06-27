from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Quizzes, Slogan, Brand
from .serializers import QuizSerializer, RandomSloganSerializer, SloganSerializer, GetRandomSloganSerializer, GetAnswerSerializer, OnlySloganSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers


class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class RandomSlogan(APIView):
    def get(self, request, format=None, **kwargs):
        slogan = Slogan.objects.filter(quiz__category=kwargs["topic"]).order_by("?")[:1]
        serializer = RandomSloganSerializer(slogan, many=True)
        return Response(serializer.data)


class QuizSlogan(APIView):
    def get(self, request, format=None, **kwargs):
        quiz = Slogan.objects.filter(quiz__category=kwargs["topic"])
        serializer = SloganSerializer(quiz, many=True)
        return Response(serializer.data)

class GetRandomSlogan(APIView):
    def get(self, request, format=None, **kwargs):
        slogan = Slogan.objects.filter(quiz__category=kwargs["topic"]).order_by("?")[:1]
        serializer = GetRandomSloganSerializer(slogan, context={'request': None}, many=True)
        return Response(serializer.data)

class SloganandBrandbyid(APIView):
    def get(self, request, format=None, **kwargs):
        brand = Slogan.objects.filter(id=kwargs["num"])
        serializer = GetAnswerSerializer(brand, context={'request': None}, many=True)
        return Response(serializer.data)

