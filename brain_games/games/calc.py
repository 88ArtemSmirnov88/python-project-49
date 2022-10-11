import random
import operator
from random import randint


def generate_random_number(first=1, second=100):
    return randint(first, second)


GAME_DESCRIPTION = "What is the result of the expression?"

ARITHMETIC_OPERATIONS = (
    ("+", operator.add),
    ("-", operator.sub),
    ("*", operator.mul)
)


def calc():
    first_num = generate_random_number()
    second_num = generate_random_number()
    sign, operation = random.choice(ARITHMETIC_OPERATIONS)
    question = "{} {} {}".format(first_num, sign, second_num)
    correct_answer = str(operation(first_num, second_num))
    return question, correct_answer
