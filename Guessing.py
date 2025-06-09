import random 


Easy_level = 10
Hard_level = 5

def check_answer(user_guess , actual_answer , turns ):
    if user_guess > actual_answer:
        print("Too High")
        return turns -1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns -1
    else:
        print(f"You got it! The answer was {actual_answer}")




def difficulty():
    level = input("Choos a diffuclty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return Easy_level
    else:
        return Hard_level
    


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of number between 1 and 100.")
    answer  = random.randint(1,100)



    turns = difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attemts remaning to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)

        if turns == 0:
            print("You've run out of guesses , you lose.:")
            return
        elif guess != answer:
            print("Guess again")

game()