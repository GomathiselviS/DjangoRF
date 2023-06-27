from rest_framework import serializers
from .models import Quizzes, Slogan, Brand


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            "title",
            "category",
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "id",
            "brand_text",
            "is_right",
        ]

class OnlySloganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slogan
        fields = [
            "id",
            "question",
        ]


class OnlyBrandtextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = [
            "id",
            "brand_text",
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

class GetRandomSloganSerializer(serializers.ModelSerializer):
    brand = OnlyBrandtextSerializer(many=True, read_only=True)


    class Meta:
        model = Slogan
        fields = [
            "id",
            "question",
            "brand",
        ]

#class GetAnswerSerializer(serializers.ModelSerializer):
#    slogan = OnlySloganSerializer(many=True, read_only=True)
#    #brand = BrandSerializer(many=True, read_only=True)
#    class Meta:
#        model = Brand
#        fields = [
#            "id",
#            #"question",
#            #"brand",
#            "get_right_answer",
#            "slogan",
#        ]

class RightBrandtextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = [
            "get_right_answer",
        ]


class GetAnswerSerializer(serializers.ModelSerializer):
    brand = RightBrandtextSerializer(many=True, read_only=True)


    class Meta:
        model = Slogan
        fields = [
            "id",
        #    "question",
            "brand",
        ]
