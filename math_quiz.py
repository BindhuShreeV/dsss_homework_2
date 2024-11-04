import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer within the specified range, inclusive.

    Args:
        min_value (int): The minimum value for the random integer.
        max_value (int): The maximum value for the random integer.

    Returns:
        int: A random integer between min_value and max_value.
    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Generates a random arithmetic operator (+, -, *).

    Returns:
        str: A random operator.
    """
    return random.choice(['+', '-', '*'])

def generate_math_problem(num1, num2, operator):
    """
    Generates a math problem string and its correct answer.

    Args:
        num1 (int): The first number in the problem.
        num2 (int): The second number in the problem.
        operator (str): The arithmetic operator.

    Returns:
        tuple: A tuple containing the problem string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Conducts a math quiz game.
    """
    score = 0
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems. Please provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = int(generate_random_integer(1, 5) + random.random())  # Cast to integer
        operator = generate_random_operator()

        problem, answer = generate_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))  # Ensure integer input
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
