from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_number(number):
    return number % 2 == 0


def get_quiz():
    question = randint(0, 100)
    answer = "yes" if even_number(question) else "no"
    return question, answer
