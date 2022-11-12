import random

from musthe import Note, Scale

enabled_scale_types = ['major', 'natural_minor']
base_notes = [x for x in Note.all()]


def random_scale_and_degree_example():
    """Returns a random scale and a random scale degree.
    """

    note = random.choice(base_notes)
    scale_type = random.choice(enabled_scale_types)
    scale = Scale(note, scale_type)
    degree = random.randint(1, len(scale.notes))
    return scale, degree, scale.notes[degree - 1]


class QuestionGenerator:

    def __init__(self):
        self.correct = 0
        self.all = 0
        self.question = None
        self.next()

    def current_question(self):
        return self.question

    def next(self):
        scale, degree, answer = random_scale_and_degree_example()
        self.question = Question((scale, degree), answer)


class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
