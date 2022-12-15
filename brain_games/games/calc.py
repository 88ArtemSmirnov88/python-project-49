from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def run():
    operators = ['+', '-', '*']
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    sign, operation = choice(operators)
    question = "{} {} {}".format(number1, sign, number2)
    correct_answer = calculate(sign, number1, number2)
    return question, str(correct_answer)


def calculate(sign, number1, number2):
    if sign == '-':
        return number1 - number2
    elif sign == '+':
        return number1 + number2
    elif sign == '*':
        return number1 * number2
