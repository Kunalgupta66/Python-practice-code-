import random

from game_data import data


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name} , a {account_descr}, from{account_country}"

def check_answer(useer_gess,a_followers,b_followers):
    if a_followers > b_followers:
        return useer_gess == "a"
    else:
        return useer_gess == "b"


score = 0
game = True
account_b = random.choice(data)

while game:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare A: {format_data(account_a)}")
    print(f"Compare B: {format_data(account_b)}")


    guess = input("Who has the more followers? Type 'A' or 'B': " ).lower()

    a_follow_count = account_a["follower_count"]
    b_follow_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follow_count,b_follow_count)

    if is_correct:
        score += 1
        print(f"You are Right! Your score is {score}")
    else:
        print("Sorry, that's wrong.")
        game = False


