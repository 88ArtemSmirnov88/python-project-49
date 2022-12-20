import math
from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def run():
    num1 = randint(2, 100)
    num2 = randint(2, 100)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer


def gcd(num1, num2):
    if not num2:
        return num1
    return gcd(num2, num1 % num2)
