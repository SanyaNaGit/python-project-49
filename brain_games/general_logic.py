import prompt

ROUNDS_COUNT = 3


def run_game(get_quiz, RULE):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(RULE)
    for i in range(ROUNDS_COUNT):
        question, correct_answer = get_quiz()
        print("Question: {}".format(question))
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(. Correct answer was '{}'.".format(
                    user_answer, correct_answer
                )
            )
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + '!')
