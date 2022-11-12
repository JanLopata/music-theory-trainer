import gui
from question_generator import QuestionGenerator

if __name__ == '__main__':
    generator = QuestionGenerator(1, 3)
    gui = gui.Gui(generator)
    gui.run()
