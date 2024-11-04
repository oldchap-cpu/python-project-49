#!/usr/bin/env python3

import prompt
from brain_games.games.is_even import is_even
from brain_games.games.what_calc import what_calc
from brain_games.games.cli import welcome_user


def main():
    name = welcome_user()
    print(f'What a game, {name}?')
    answer = prompt.string("\"even-number\", push \'1\'\n\"calculator\", push \'2\'\notherwise, push \'any key\'\n\033[33m>>> ")
    print("\033[0m")
    if answer == '1' or answer == '2':
        match answer:
            case '1':
                is_even(name)
            case '2':
                what_calc(name)
    else:
        print('Sorry... see you later!')


if __name__ == '__main__':
    main()
