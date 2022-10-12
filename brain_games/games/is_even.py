from random import randint


DESCRIPTION = '''Answer "yes" if the number is even, otherwise answer "no".'''


def run():
    number = randint(1, 200)
    question = f'Question: {number}'
    answer = correct_answer(number)
    return question, answer


def correct_answer(number):
    return 'no' if number % 2 else 'yes'
