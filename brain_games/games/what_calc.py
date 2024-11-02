def what_calc(name):

    import prompt
    import random

# start game, push " 2 "
    print("What is the result of the expression?")
    i = 0
    while i < 3:
        number_1 = str(random.randint(0, 20))
        number_2 = str(random.randint(0, 20))
        operator = random.choice(['+', '-', '*'])
        print(f"Question: {number_1} {operator} {number_2}")
        result = eval(number_1 + operator + number_2)
        answer = prompt.string('Your answer \033[033m>>> ')
        print("\033[0m")
        if answer == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer was {result}. \n"
                  f"Let's try again, {name}!")
            break

    if i == 3:
        print(f"Congratulations, {name}!")
