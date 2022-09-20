from random import randint
import prompt


def brain_even_game(game):
    # шаг 1: поздороваться
    print('Welcome to the Brain Games!')
    # шаг 2: спросить имя
    name = prompt.string('May I have your name?')
    # шаг 3: поздороваться + имя
    print(f'Hello, {name}!')
    # шаг 4: задает вопрос нужной игры
    index = 0
    score = 3
    while index < score:
        question, correct_answer = game()
        print(question)
        # шаг 5: читает ответ
        answer = prompt.string('Your answer: ')
        # шаг 6: сравнение ответа с правильным
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
        # шаг 7: увеличивается кол-во очков (если верно) - переход в следующий раунд
        index += 1
        # шаг 8: игра завершается
    print(f'Congratulations, {name}!')


def game():
    random_number = randint(1, 200)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = (f"""Answer "yes" if the number is even, otherwise answer "no".
    Question: {random_number}""")
    return question, correct_answer