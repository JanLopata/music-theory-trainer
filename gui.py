import curses
from curses import wrapper
from enum import Enum

import question_formatter
from question_generator import QuestionGenerator

generator = None
gui_phase = None
TOP = 2


def half_length(answer):
    return int((len(answer) - 1) / 2)


class Gui:

    def __init__(self, question_generator: QuestionGenerator):
        self.generator = question_generator
        self.gui_phase = GuiPhase.PROVIDE_QUESTION
        self.tempo = 30
        self.beats = 4
        self.stars = -1

    def run(self):
        wrapper(self.main)

    def main(self, screen):

        curses.curs_set(0)

        key = ord(' ')
        while key != ord('q'):
            screen.timeout(int(1000 * 60 / self.tempo / self.beats))
            key = screen.getch()

            self.stars += 1

            if self.stars > self.beats:
                self.stars = 1
                self.next_gui_phase()

            screen.clear()
            self.show_question(screen)
            self.show_stars(screen)
            if self.gui_phase == GuiPhase.PROVIDE_ANSWER:
                self.show_answer(screen)

    def show_answer(self, screen):
        answer = question_formatter.format_answer(self.generator.current_question(), 'cz')
        screen.addstr(TOP + 2, 10 - half_length(answer), answer)

    def show_question(self, screen):
        question = question_formatter.format_question(self.generator.current_question(), 'cz')
        screen.addstr(TOP, 11 - half_length(question), question)

    def show_stars(self, screen):
        screen.addstr(TOP + 1, 9, "*" * self.stars)

    def next_gui_phase(self):

        if self.gui_phase == GuiPhase.PROVIDE_QUESTION:
            # provide answer
            self.gui_phase = GuiPhase.PROVIDE_ANSWER
            return

        if self.gui_phase == GuiPhase.PROVIDE_ANSWER:
            # provide question
            self.generator.next()
            self.gui_phase = GuiPhase.PROVIDE_QUESTION
            return


class GuiPhase(Enum):
    PROVIDE_QUESTION = 1
    PROVIDE_ANSWER = 2
