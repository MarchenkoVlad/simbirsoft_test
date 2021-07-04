def serializers(choices):
    result = dict()
    ans_list = []

    for choice in choices:
        result['question_text'] = choice.question.text
        ans = {
            "text": choice.text,
            "id": choice.id,
            "is_correct": choice.is_correct,
            "answer_checked": False,
        }
        ans_list.append(ans)
    result['choices'] = ans_list

    return result
