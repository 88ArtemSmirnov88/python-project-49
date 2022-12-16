from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def run():
    operators = ['+', '-', '*']
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    operation = choice(operators)
    question = f'Question: {number1} {operation} {number2}'
    correct_answer = calculate(operation, number1, number2)
    return question, str(correct_answer)


def calculate(operation, number1, number2):
    if operation == '-':
        return number1 - number2
    elif operation == '+':
        return number1 + number2
    elif operation == '*':
        return number1 * number2
