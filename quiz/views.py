from rest_framework import generics
from rest_framework.response import Response
from .models import Quizzes, Question
from .serializers import QuizSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView

#Quiz End Point (return all objects)
class Quiz(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


#Random Enpoint
class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        #from Question (where all questions are stored), the argument is whatever the quiz topic is
        #__ means moving backwards, we order by ? , meaning we randomise
        question = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        #Then we have a randomQuestionSerializer
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


#we dont order  we just get all the question for that quiz
class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)