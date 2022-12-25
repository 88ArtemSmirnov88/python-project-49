from random import randint, choice


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def make_progression(ini_number, step, max_number):
    return range(ini_number, max_number, step)


def generate():
    initial_number = randint(1, 100)
    step = randint(1, 10)
    maximum_number = (step * PROGRESSION_LENGTH) + initial_number
    progression = make_progression(initial_number, step, maximum_number)
    hidden_element = choice(progression)
    progression = ' '.join([
        '..' if item == hidden_element else str(item) for item in progression
    ])
    question = f'{progression}'
    return question, str(hidden_element)
