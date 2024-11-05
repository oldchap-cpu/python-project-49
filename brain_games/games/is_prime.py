
def is_prime(name):    # start brain-prime

    import prompt
    import random

    def body(number):
        if number <= 1:
            return False, 1
        if number in (2, 3, 5, 7):
            return True, number
        if number % 2 == 0:
            dv = 2
            return False, 2
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                dv = i
                return False, dv
        return True, number

    print("Answer \"yes\" if the number is prime, otherwise answer \"no\".")
    i = 0
    while i < 3:
        number = random.randint(0, 99)
        print("Question: " + str(number))
        answer = prompt.string('\033[0mYour answer \033[033m>>> ')
        print("\033[0m")
        if answer != 'yes' and answer != 'no':
            print("Let's try again, " + name + "!")
            break
        result, item = body(number)
        if result is True:
            match answer:
                case 'yes':
                    print('Correct!\n')
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
                          f"How about {number} : {item}? :)\n"
                          f"Let's try again, {name}!")
                    break
                case 'no':
                    print('Correct!\n')
                    i += 1
    if i == 3:
        print(f"Congratulations, {name}!")
