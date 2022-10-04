import prompt


SCORE = 3


def logic(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    index = 0
    while index < SCORE:
        question, correct_answer = game()
        print(question)
        answer = prompt.string('Your answer: ')
        answer = answer.lower()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        index += 1
    print(f'Congratulations, {name}!')
