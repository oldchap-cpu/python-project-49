def welcome_user():

    from colorama import Fore, Back, Style
    import prompt

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name, boy?" + Fore.YELLOW + ">>> ")
    print(Style.RESET_ALL)
    print(f'Hello, {name}!')
    return name
