from .dto import ChoiceDTO, QuestionDTO, QuizDTO, AnswerDTO, AnswersDTO
from typing import List


class QuizResultService():
    def __init__(self, quiz_dto: QuizDTO, answers_dto: AnswersDTO):
        self.quiz_dto = quiz_dto
        self.answers_dto = answers_dto

    def get_result(self) -> float:
        answers_list = []
        questions_dto = self.quiz_dto.questions
        answers = {
            answer.question_uuid: answer.choices
            for answer in self.answers_dto.answers
        }
        questions = {
            question.uuid: question.choices
            for question in questions_dto
        }

        for question_uuid, answer_choices in answers.items():
            choices = questions[question_uuid]
            choices_correct = get_correct_choices_ids(choices)

            if answer_choices == choices_correct:
                answers_list.append(1)
        result = answers_list.count(1) / len(questions_dto)
        return result


def get_correct_choices_ids(choices):
    choice_ids = []

    for choice in choices:
        if choice.is_correct:
            choice_ids.append(choice.uuid)
    return choice_ids
