from random import randint
from brain_games.general_logic import game


rule = 'Answer "yes" if number even otherwise answer "no".'


def even_number(number):
    return number % 2 == 0


def get_quiz():
    question = randint(0, 100)
    answer = "yes" if even_number(question) else "no"
    return question, answer


def run_game():
    game(get_quiz, rule)
