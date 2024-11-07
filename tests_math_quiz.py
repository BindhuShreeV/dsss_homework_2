import unittest
from math_quiz import generate_random_number, generate_random_operation, create_math_problem

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_number(self):
        """Tests if the generated random number is within the specified range."""
        min_val, max_val = 1, 10
        for _ in range(100):
            random_number = generate_random_number(min_val, max_val)
            self.assertTrue(min_val <= random_number <= max_val)

    def test_generate_random_operation(self):
        """Tests if the generated operator is one of '+', '-', or '*'."""
        valid_operators = ['+', '-', '*']
        for _ in range(100):
            operator = generate_random_operation()
            self.assertIn(operator, valid_operators)

    def test_create_math_problem(self):
        """Tests math problem creation and correct answer calculation."""
        test_cases = [
            (5, 2, '+', "5 + 2", 7),
            (7, 3, '-', "7 - 3", 4),
            (4, 6, '*', "4 * 6", 24),
            (0, 5, '+', "0 + 5", 5),
            (10, 2, '-', "10 - 2", 8),
            (3, 0, '*', "3 * 0", 0),
        ]

        for operand1, operand2, operation, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(operand1, operand2, operation)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == '__main__':
    unittest.main()
