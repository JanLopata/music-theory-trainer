import random

from musthe import Note, Scale

available_scale_types = ['major', 'natural_minor']
circle_of_quint = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#']
circle_of_quart = ['C', 'F', 'Bb', 'Eb', 'Ab', 'Db', 'Gb', 'Cb']
# zip flat the two lists together
combination = [item for sublist in zip(circle_of_quint, circle_of_quart) for item in sublist]
base_notes = [Note(f'{note}4') for note in combination]


def random_scale_and_degree_example(scale_level: int, note_level: int):
    """Returns a random scale and a random scale degree.
    """

    notes_on_level = base_notes[1:(note_level + 1) * 2]
    note = random.choice(notes_on_level)
    scale_type = random.choice(available_scale_types[0:scale_level])
    scale = Scale(note, scale_type)
    degree = random.randint(1, len(scale.notes))
    return scale, degree, scale.notes[degree - 1]


class QuestionGenerator:

    def __init__(self, scale_level: int, note_level: int):
        self.correct = 0
        self.all = 0
        self.question = None
        self.scale_level = scale_level
        self.note_level = note_level
        self.next()

    def current_question(self):
        return self.question

    def next(self):
        scale, degree, answer = random_scale_and_degree_example(self.scale_level, self.note_level)
        self.question = Question((scale, degree), answer)


class Question:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
