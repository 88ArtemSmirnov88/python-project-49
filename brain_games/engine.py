import prompt

NUMBER_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    print(game.DESCRIPTION)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    count = 0
    while count < NUMBER_OF_ROUNDS:
        question, correct_answer = game.run()
        print('Question:', question)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
        count += 1
    print(f'Congratulations, {name}!')
