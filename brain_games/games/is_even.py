from random import randint


DESCRIPTION = '''Answer "yes" if the number is even, otherwise answer "no".'''


def run():
    answers = ['no', 'yes']
    number = randint(1, 200)
    question = f'Question: {number}'
    correct_answer = answers[is_even(number)]
    return question, correct_answer


def is_even(number):
    return number % 2 == 0
