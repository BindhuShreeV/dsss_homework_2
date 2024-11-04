import unittest
from math_quiz import generate_random_integer, generate_random_operator, generate_math_problem

class TestMathQuiz(unittest.TestCase):

    def test_generate_random_integer(self):
        """Test if the generated random integer is within the specified range."""
        min_val, max_val = 1, 10
        for _ in range(100):  # Test multiple times to ensure randomness stays in range
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"Random integer {rand_num} out of range")

    def test_generate_random_operator(self):
        """Test if the generated operator is one of '+', '-', or '*'."""
        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Test multiple times for randomness
            operator = generate_random_operator()
            self.assertIn(operator, valid_operators, f"Generated invalid operator {operator}")

    def test_generate_math_problem(self):
        """Test math problem generation and correctness of the answer."""
        test_cases = [
            (5, 2, '+', "5 + 2", 7),
            (7, 3, '-', "7 - 3", 4),
            (4, 6, '*', "4 * 6", 24),
            (0, 5, '+', "0 + 5", 5),
            (10, 2, '-', "10 - 2", 8),
            (3, 0, '*', "3 * 0", 0),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem, f"Generated problem string '{problem}' is incorrect")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer}, but got {answer}")

if __name__ == "__main__":
    unittest.main()
