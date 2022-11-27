import curses
from curses import wrapper
from enum import Enum

import question_formatter
from question_generator import QuestionGenerator

generator = None
gui_phase = None


def half_length(answer):
    return int(len(answer) / 2)


class Gui:

    def __init__(self, question_generator: QuestionGenerator):
        self.generator = question_generator
        self.gui_phase = GuiPhase.PROVIDE_QUESTION
        self.tempo = 45

    def run(self):
        wrapper(self.main)

    def main(self, screen):

        self.show_question(screen)

        key = ord(' ')
        while key != ord('q'):
            screen.timeout(int(1000 * 60 / self.tempo))
            key = screen.getch()
            # if key is space or return, then provide result and read result

            if self.gui_phase == GuiPhase.PROVIDE_QUESTION:
                if True or key == curses.KEY_ENTER or key == ord(' '):
                    # provide answer
                    self.gui_phase = GuiPhase.PROVIDE_ANSWER
                    screen.clear()
                    self.show_question(screen)
                    self.show_answer(screen)
                    continue

            if self.gui_phase == GuiPhase.PROVIDE_ANSWER:
                if True or key == curses.KEY_ENTER or key == ord(' '):
                    # provide question
                    self.gui_phase = GuiPhase.PROVIDE_QUESTION
                    screen.clear()
                    self.generator.next()
                    self.show_question(screen)
                    continue

    def show_answer(self, screen):
        answer = question_formatter.format_answer(self.generator.current_question(), 'cz')
        screen.addstr(5, 10 - half_length(answer), answer)

    def show_question(self, screen):
        question = question_formatter.format_question(self.generator.current_question(), 'cz')
        screen.addstr(4, 10 - half_length(question), question)


class GuiPhase(Enum):
    PROVIDE_QUESTION = 1
    PROVIDE_ANSWER = 2
