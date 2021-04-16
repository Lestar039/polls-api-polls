from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Question, Answer
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer
from django.utils import timezone


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET'])
def polls_list(request):
    poll = Poll.objects.all()
    serializer = PollSerializer(poll, many=True)
    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def polls_active_list(request):
    poll = Poll.objects.filter(start_date__lte=timezone.now()).filter(finish_date__gte=timezone.now())
    serializer = PollSerializer(poll, many=True)
    return Response(serializer.data)


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET'])
def poll_detail(request, pk):
    poll = get_object_or_404(Poll, id=pk)
    serializer = PollSerializer(poll, many=False)
    return Response(serializer.data)


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET', 'POST'])
def poll_create(request):
    serializer = PollSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET', 'PUT'])
def poll_update(request, pk):
    poll = get_object_or_404(Poll, id=pk)
    serializer = PollSerializer(instance=poll, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET', 'DELETE'])
def poll_delete(request, pk):
    poll = get_object_or_404(Poll, id=pk)
    poll.delete()
    return Response("Item successfully delete!")


# >>>>>>>> Question <<<<<<<<<<<<
@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET'])
def questions_list(request, pk):
    poll = get_object_or_404(Poll, id=pk)
    questions = Question.objects.filter(poll=poll)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def question_detail(request, pk):
    question = get_object_or_404(Question, id=pk)
    serializer = QuestionSerializer(question, many=False)
    return Response(serializer.data)


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET', 'POST'])
def question_create(request):
    serializer = QuestionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET', 'PUT'])
def question_update(request, pk):
    question = get_object_or_404(Question, id=pk)
    serializer = QuestionSerializer(instance=question, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@permission_classes((IsAuthenticated, IsAdminUser))
@api_view(['GET', 'DELETE'])
def question_delete(request, pk):
    question = get_object_or_404(Question, id=pk)
    question.delete()
    return Response("Item successfully delete!")


# >>>>>>> Answer <<<<<<
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def answer_create(request):
    serializer = AnswerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def users_answer(request, pk):
    answers = Answer.objects.filter(author=pk)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)
