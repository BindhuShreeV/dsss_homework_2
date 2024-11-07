import random

def generate_random_number(min_value, max_value):
    """Generates a random integer within the specified range (inclusive)."""
    return random.randint(min_value, max_value)

def generate_random_operation():
    """Generates a random arithmetic operator (+, -, *)."""
    return random.choice(['+', '-', '*'])

def create_math_problem(operand1, operand2, operation):
    """Creates a math problem string and its solution."""
    problem_string = f"{operand1} {operation} {operand2}"
    if operation == '+':
        solution = operand1 + operand2
    elif operation == '-':
        solution = operand1 - operand2
    else:
        solution = operand1 * operand2
    return problem_string, solution

def math_quiz():
    """Conducts a math quiz game."""
    score = 0
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems. Please provide the correct answers.")

    for _ in range(total_questions):
        first_number = generate_random_number(1, 10)
        second_number = generate_random_number(1, 5) + random.random()  # Cast to integer later
        arithmetic_operation = generate_random_operation()

        problem, answer = create_math_problem(first_number, second_number, arithmetic_operation)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct   
 answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()   
