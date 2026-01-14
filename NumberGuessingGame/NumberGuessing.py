import random
import logoart
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_choosen):
    if level_choosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_choosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high")
        return attempts-1
    else:
        print(f"Your guess is right......The answer was {answer}.")
def game():
    print(logoart.logo)
    print("Let me think a number b/w 1 to 100")
    answer=random.randint(1,100)
    level=input("Choose level of difficulty.....'easy' or 'hard':")
    attempts=set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("You enterd wrong difficulty level....")
        return
    guessed_number=0
    while guessed_number!=answer:
        print(f"You have {attempts} remaining to guees the number:")
        guessed_number=int(input("Enter the number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("You are out of guesses....Better luck next time")
            return
        elif guessed_number!=answer:
            print("Guess Again")
game()
