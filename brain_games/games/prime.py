from random import randrange

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    index = 1
    count = 0
    while index <= num // 2:
        if num % index == 0:
            count += 1
        index += 1
    return count == 1


def get_quiz():
    question = randrange(1, 100)
    answer = "yes" if is_prime(question) else "no"
    return question, answer
