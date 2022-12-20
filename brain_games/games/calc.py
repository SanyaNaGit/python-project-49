from random import choice, choices
from brain_games.general_logic import game

rule = 'What is the result of the expression?'


def get_quiz():
    sign = choice(["*", "+", "-"])

    def expression(num_1, num_2, sign):
        if sign == "*":
            result = num_1 * num_2
        elif sign == "+":
            result = num_1 + num_2
        elif sign == "-":
            result = num_1 - num_2
        return result

    num1, num2 = choices(range(1, 100), k=2)
    answer = expression(num1, num2, sign)
    question = "{} {} {}".format(num1, sign, num2)
    return question, str(answer)


def run_game():
    game(get_quiz, rule)
