from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'

LENGTH = 10


def make_progression():
    initial_number = randint(1, 100)
    delta = randint(1, 25)
    maximum_number = (delta * LENGTH) + initial_number
    return range(initial_number, maximum_number, delta)


def run():
    prog = make_progression()
    secret = choice(prog)
    progression = ' '.join([
        '..' if num == secret else str(num) for num in prog
    ])
    question = f'{progression}'
    return question, str(secret)
