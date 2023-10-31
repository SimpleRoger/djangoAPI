from rest_framework import serializers
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    #this is what we want to pass into the front end
    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    #String related Field
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        #title of the question + answer
        fields = [
            'title','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    #not iterable so many is not equal true
    quiz = QuizSerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'quiz','title','answer',
        ]