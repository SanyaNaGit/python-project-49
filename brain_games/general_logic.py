import prompt


def game(get_quiz, rule):
    counter = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(rule)
    for i in range(counter):
        question, correct_answer = get_quiz()
        print("Question: {}".format(question))
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, correct_answer))
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + '!')
