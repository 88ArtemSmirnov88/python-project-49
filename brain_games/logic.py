from random import randint
import prompt


def logic(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?')
    print(f'Hello, {name}!')
    index = 0
    score = 3
    while index < score:
        question, correct_answer = game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        index += 1
    print(f'Congratulations, {name}!')


def is_even():
    random_number = randint(1, 200)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = (f"""Answer "yes" if the number is even, otherwise answer "no".
    Question: {random_number}""")
    return question, correct_answer
