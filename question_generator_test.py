import unittest

from question_generator import QuestionGenerator


class MyTestCase(unittest.TestCase):
    def test_init(self):
        generator = QuestionGenerator(1, 7)
        assert generator is not None


if __name__ == '__main__':
    unittest.main()
