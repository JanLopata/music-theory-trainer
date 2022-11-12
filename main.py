import gui
from question_generator import QuestionGenerator

if __name__ == '__main__':
    generator = QuestionGenerator()
    gui = gui.Gui(generator)
    gui.run()
