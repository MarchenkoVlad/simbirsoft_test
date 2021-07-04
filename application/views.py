from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from quiz.services import QuizResultService
from .models import Question, Choice, Answer
from .serializers import serializers
from .query import (
    get_choices_by_question,
    save_answers_in_db, get_answers_by_guid,
    get_all_question_id,  get_questions, make_questions_dto,
    make_answers_dto, make_quiz_dto, make_answer_list_dto,
    get_question_by_guid
)
from .session import save_session, get_session_key
from .services import check_type_question, checking_answer


def home(request):
    all_question_id = list(get_all_question_id())
    min_question_id = min(all_question_id)
    context = {
        'min_question_id': min_question_id
    }
    return render(request, 'application/home.html', context)


def index(request, pk):
    save_session(request)
    guid = get_session_key(request)

    choices = get_choices_by_question(pk)
    answers = get_answers_by_guid(guid, pk)
    serialize_choices = serializers(choices)
    choice_type = check_type_question(serialize_choices)

    if answers:
        serialize_choices = checking_answer(answers, serialize_choices)

    all_question_id = list(get_all_question_id())
    min_question_id = min(all_question_id)
    max_question_id = max(all_question_id)

    try:
        prev = all_question_id[all_question_id.index(pk) - 1]
    except IndexError as e:
        prev = None
    try:
        next = all_question_id[all_question_id.index(pk) + 1]
    except IndexError as e:
        next = None

    context = {
        'choice': serialize_choices,
        'choice_flag': choice_type,
        'question_id': pk,
        'prev': prev,
        'next': next,
        'min_question_id': min_question_id,
        'max_question_id': max_question_id,
    }
    return render(request, 'application/index.html', context)


def save_answer(request):
    save_session(request)
    guid = get_session_key(request)
    question_id = int(request.POST['question'])
    choices = request.POST.getlist('form')

    if not question_id or not choices:
        return HttpResponse(status=400)

    save_answers_in_db(guid, choices, question_id)
    return HttpResponse(status=201)


def report(request):
    guid = get_session_key(request)
    questions = get_questions()
    questions_dto = make_questions_dto(questions)
    quiz_dto = make_quiz_dto(questions_dto)
    answer_list_dto = make_answer_list_dto(questions, guid)
    answers_dto = make_answers_dto(answer_list_dto, quiz_dto.uuid)

    quiz = QuizResultService(quiz_dto, answers_dto)
    result = quiz.get_result()

    all_question_id = list(get_all_question_id())
    min_question_id = min(all_question_id)

    context = {
        'statistics': int(result * 100),
        'min_question_id': min_question_id
    }
    return render(request, 'application/report.html', context)
