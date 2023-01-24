from random import choice, choices

RULE = 'What is the result of the expression?'


def get_quiz():
    sign = choice(["*", "+", "-"])
    num1, num2 = choices(range(1, 100), k=2)
    if sign == "*":
        result = num1 * num2
    elif sign == "+":
        result = num1 + num2
    elif sign == "-":
        result = num1 - num2
    answer = result
    question = "{} {} {}".format(num1, sign, num2)
    return question, str(answer)
