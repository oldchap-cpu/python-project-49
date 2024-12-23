def is_even(name):

    import prompt
    import random

    # start game
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    i = 0
    while i < 3:
        number = random.randint(0, 99)
        print("Question: " + str(number))
        answer = prompt.string('Your answer \033[033m>>> ')
        print("\033[0m")
        if answer != 'yes' and answer != 'no':
            print("Let's try again, " + name + "!")
            break
        if int(number) % 2 == 0:
            match answer:
                case 'yes':
                    print('Correct!')
                    i += 1
                case 'no':
                    print(f"\'no\' is wrong answer ;(. "
                          f"Correct answer was \'yes\'. \n"
                          f"Let's try again, {name}!")
                    break
        else:
            match answer:
                case 'yes':
                    print(f"\'yes\' is wrong answer ;(. "
                          f"Correct answer was \'no\'. \n"
                          f"Let's try again, {name}!")
                    break
                case 'no':
                    print('Correct!')
                    i += 1
    if i == 3:
        print(f"Congratulations, {name}!")
