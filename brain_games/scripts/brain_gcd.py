from brain_games.games.gcd import get_quiz, RULE
from brain_games.general_logic import run_game


def main():
    run_game(get_quiz, RULE)


if __name__ == '__main__':
    main()
