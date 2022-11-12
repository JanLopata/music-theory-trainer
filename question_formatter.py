from question_generator import Question, QuestionScheme


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
        return str(question.answer)

    return 'Not implemented yet.'
