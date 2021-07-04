def check_type_question(choices):
    current_choices = choices['choices']
    list_choice = []

    for choice in current_choices:
        list_choice.append(choice['is_correct'])

    if list_choice.count(1) > 1:
        return True


def checking_answer(answers, serialize_choices):
    for answer in answers:
        choice_id = answer.choice.id
        current_choices = serialize_choices['choices']

        for current_choice in current_choices:
            if current_choice["id"] == choice_id:
                current_choice["answer_checked"] = True
    return serialize_choices
