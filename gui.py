import curses
from curses import wrapper
from enum import Enum

from question_generator import QuestionGenerator

generator = None
gui_phase = None


class Gui:

    def __init__(self, question_generator: QuestionGenerator):
        self.generator = question_generator
        self.gui_phase = GuiPhase.PROVIDE_QUESTION

    def run(self):
        wrapper(self.main)

    def main(self, stdscr):

        stdscr.addstr(15, 20, str(self.generator.current_question().question))

        key = ''
        while key != ord('q'):
            key = stdscr.getch()
            # if key is space or return, then provide result and read result

            if self.gui_phase == GuiPhase.PROVIDE_QUESTION:
                if key == curses.KEY_ENTER or key == ord(' '):
                    # provide answer
                    self.gui_phase = GuiPhase.PROVIDE_ANSWER
                    stdscr.addstr(15, 20, str(self.generator.current_question().answer))
                    continue

            if self.gui_phase == GuiPhase.PROVIDE_ANSWER:
                if key == curses.KEY_ENTER or key == ord(' '):
                    # provide question
                    self.gui_phase = GuiPhase.PROVIDE_QUESTION
                    self.generator.next()
                    stdscr.clear()
                    stdscr.addstr(14, 20, str(self.generator.current_question().question))
                    continue

            stdscr.addstr(0, 0, f'You pressed {key}. State is {self.gui_phase}  ')


class GuiPhase(Enum):
    PROVIDE_QUESTION = 1
    PROVIDE_ANSWER = 2
