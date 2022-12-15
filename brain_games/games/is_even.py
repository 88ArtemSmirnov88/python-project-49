from random import randint


DESCRIPTION = '''Answer "yes" if the number is even, otherwise answer "no".'''


def run():
    number = randint(1, 200)
    question = f'Question: {number}'
    answer = is_even(number)
    return question, answer


def is_even(number):
    return 'no' if number % 2 else 'yes'
