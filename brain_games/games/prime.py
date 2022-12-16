from random import randint


DESCRIPTION = '''Answer "yes" if given number is prime.
                 Otherwise answer "no".'''


def is_prime(number):
    for i in range(2, number, 1):
        if number % i == 0 or number == 1:
            return False
    return True


def run():
    number = randint(1, 100)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'Question: {number}'
    return question, correct_answer
