from question_generator import Question, QuestionScheme

note_dict = {
    "cz": {'B': 'H'}
}


def format_question(question: Question, language: str):
    """Format a question for display.

    Args:
        question: A question object.

    Returns:
        A string representing the question.
    """

    if question.scheme == QuestionScheme.SCALE_DEGREE_EQUALS_NOTE:
        scale, degree = question.question
        return f'{scale.root} {scale.name} {degree}.'

    return 'Not implemented yet.'


def format_answer(question: Question, language: str):
    """Format an answer for display.

    Args:
        question: A question object.

    Returns:
        A string representing the answer.
    """

    if question.scheme == QuestionScheme.SCALE_DEGREE_EQUALS_NOTE:
        return format_note(str(question.answer), language)

    return 'Not implemented yet.'


def format_note(note: str, language: str):
    result = note
    if language in note_dict:
        lan_dict = note_dict[language]
        if note in lan_dict:
            result = lan_dict[note]

    return result.replace("b", '♭').replace("#", '♯')
