def gcf_game(name):

    import random
    import prompt

    def gcf_recursion(a, b):
        if a == 0:
            return b
        a, b = b, a
        return gcf_recursion(a % b, b)

    print("Find the greatest common divisor of given numbers")
    i = 0
    while i < 3:
        number_1 = random.randint(0, 20)
        number_2 = random.randint(0, 20)
        print(f'Question: {number_1} and {number_2}')
        gcf = gcf_recursion(number_1, number_2)
        answer = prompt.string("Your answer: \033[033m>>> \033[0m")
        if gcf == int(answer):
            print("Correct!")
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{gcf}'")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f"Congratulations, {name}!")
    else:
        print("Sorry... See you later)")
