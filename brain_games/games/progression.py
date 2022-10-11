from random import randint


def progression():
    list = []
    start = randint(1, 20)
    step = randint(1, 10)
    end = start + (10 * step)

    for i in range(start, end, step):
        list.append(str(i))

    limit = len(list) - 1

    correct_answer_index = randint(1, limit)
    correct_answer = list[correct_answer_index]
    list[correct_answer_index] = ".."
    question = (f'''What number is missing in the progression?
Question: {' '.join(list)}''')
    return question, correct_answer
