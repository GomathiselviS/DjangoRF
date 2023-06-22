from rest_framework import serializers
from .models import Quizzes, Slogan, Brand


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            "title",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "brand_text",
            "is_right",
        ]


class RandomSloganSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=True, read_only=True)

    class Meta:
        model = Slogan
        fields = [
            "question",
            "brand",
        ]


class SloganSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Slogan
        fields = [
            "quiz",
            "question",
            "brand",
        ]
