#!/usr/bin/env python3
import prompt
from random import randint


def even(number):
    return number % 2 == 0


def quiz():
    question = randint(0, 100)
    answer = "yes" if even(question) else "no"
    return question, answer


def game():
    count = 3
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(count):
        question, correct_answer = quiz()
        print("Question: {}".format(question))
        user_answer = input("Your answer: ")
        if correct_answer == user_answer:
            print('Correct!')
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, " + name + "!")
            return
    print('Congratulations, ' + name + '!')


def main():
    game()


if __name__ == '__main__':
    maim()
