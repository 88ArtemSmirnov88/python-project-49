from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate():
    number = randint(1, 200)
    question = f'{number}'
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def is_even(number):
    return number % 2 == 0
