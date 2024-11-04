def progression_game(name):

    import random
    import prompt

    print("What number is missing in the progression?")
    i = 0
    while i < 3:
        rate_list = random.randint(2, 5)   # выбираем прогрессию списка
        series = list()
        item = 0
        for n in range(0, 10):             # создаем список значений с случайной прогрессией
            item += rate_list
            series.append(item)
        index = int(random.randint(0, 9))  # выбираем индекс под замену
        value = series[index]              # сохраняем скрытое значение
        series[index] = '..'               # скрываем значение
        print("Question: ", *series)
        answer = prompt.string("Your answer: \033[033m>>> \033[0m")
        if value == int(answer):
            print("Correct!")
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{value}'")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f"Congratulations, {name}!")
    else:
        print("Sorry... See you later)")
