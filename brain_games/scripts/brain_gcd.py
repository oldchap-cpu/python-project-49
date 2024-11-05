#!/usr/bin/env python3

import prompt

from brain_games.games.gcf_game import gcf_game
from brain_games.games.cli import welcome_user


def main():
    name = welcome_user()
    print(f'Do you want a game, {name}?')
    answer = prompt.string("yes[y], no[any key]\n\033[33m>>> ")
    print("\033[0m")
    if answer == 'y' or answer == 'yes':
        gcf_game(name)
    else:
        print('Sorry... see you later!')


if __name__ == '__main__':
    main()
