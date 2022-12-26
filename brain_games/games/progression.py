from random import randint
from brain_games.general_logic import game

rule = 'What number is missing in the progression?'

progression_length = 10


def get_progression(start, step, progression_length):
    stop = start + (progression_length * step)
    progression = list(range(start, stop, step))
    return progression


def get_quiz():
    start = randint(1, 100)
    step = randint(1, 10)
    miss_item_index = randint(1, progression_length - 1)
    progression = get_progression(start, step, progression_length)
    answer = progression.pop(miss_item_index)
    progression.insert(miss_item_index, "..")
    question = " ".join([str(i) for i in progression])
    return question, str(answer)


def run_game():
    game(get_quiz, rule)
