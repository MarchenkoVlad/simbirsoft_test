from typing import List

from django.db.models.query import QuerySet

from quiz.dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from .models import Choice, Question, Answer


def get_choices_by_question(question: Question):
    choices = Choice.objects.select_related('question').filter(
        question=question
    )
    return choices


def get_answers_by_guid(guid: str, question: Question):
    answers = Answer.objects.filter(question=question, user_id=guid)
    return answers


def save_answers_in_db(guid: str, choices: List[str], question_id: int):
    question = Question.objects.get(pk=question_id)
    check_answer = check_user_answer_exist(guid, question)

    if check_answer:
        delete_user_answer(check_answer)

    for choice_id in choices:
        choice = Choice.objects.get(pk=choice_id)
        answers, created = Answer.objects.update_or_create(
            question=question, choice=choice, user_id=guid
        )
        answers.save()

    return answers


def check_user_answer_exist(guid: str, question: Question):
    user_answer = Answer.objects.filter(user_id=guid, question=question)
    return user_answer


def delete_user_answer(user_answer: QuerySet):
    for elem in user_answer:
        elem.delete()


def get_all_question_id():
    all_question_id = Question.objects.values_list('id', flat=True)
    return all_question_id


def get_questions():
    questions = Question.objects.all()
    return questions


def get_question_by_guid(guid: str):
    answers = Answer.objects.filter(user_id=guid)
    questions = [answer.question for answer in answers]
    return questions


def make_choices_dto(question: Question) -> List[ChoiceDTO]:
    choices_dto = [
        ChoiceDTO(choice.id, choice.text, choice.is_correct)
        for choice in question.choice_set.all()
    ]
    return choices_dto


def make_questions_dto(questions: List[Question]) -> List[QuestionDTO]:
    questions_dto = [
        QuestionDTO(question.id, question.text, make_choices_dto(question))
        for question in questions
    ]
    return questions_dto


def make_quiz_dto(questions_dto: List[QuestionDTO]) -> QuizDTO:
    quiz_dto = QuizDTO('1', 'quiz', questions_dto)
    return quiz_dto


def make_answer_dto(choices: List[str], question_id: str) -> AnswerDTO:
    answer_dto = AnswerDTO(question_id, choices)
    return answer_dto


def make_answers_dto(
        answer_list_dto: List[AnswerDTO],
        quiz_uuid: str) -> AnswersDTO:
    answers_dto = AnswersDTO(quiz_uuid, answer_list_dto)
    return answers_dto


def make_answer_list_dto(
        questions: List[Question],
        guid: str) -> List[AnswerDTO]:
    answer_list_dto = []

    for question in questions:
        choices = []
        answers = question.answer_set.all().filter(user_id=guid)

        for answer in answers:
            choices += get_choices_from_answer(answer)
        answer_list_dto.append(make_answer_dto(choices, question.id))

    return answer_list_dto


def get_choices_from_answer(answer: Answer) -> List[Choice]:
    choices = answer.choice.id
    return [choices]
