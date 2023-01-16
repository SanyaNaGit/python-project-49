from random import choice, choices

RULE = 'What is the result of the expression?'


def get_quiz():
    sign = choice(["*", "+", "-"])

    def expression(num_1, num_2):
        if sign == "*":
            result = num_1 * num_2
        elif sign == "+":
            result = num_1 + num_2
        elif sign == "-":
            result = num_1 - num_2
        return result

    num1, num2 = choices(range(1, 100), k=2)
    answer = expression(num1, num2)
    question = "{} {} {}".format(num1, sign, num2)
    return question, str(answer)
