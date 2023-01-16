from random import randint

RULE = 'What number is missing in the progression?'

PROGRESSION_LENGTH = 10


def get_progression(start, step):
    stop = start + (PROGRESSION_LENGTH * step)
    progression = list(range(start, stop, step))
    return progression


def get_quiz():
    start = randint(1, 100)
    step = randint(1, 10)
    random_index = randint(1, PROGRESSION_LENGTH - 1)
    progression = get_progression(start, step)
    answer = progression[random_index]
    progression[random_index] = '..'
    question = " ".join([str(i) for i in progression])
    return question, str(answer)
