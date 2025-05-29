import random

stages = ["💔", "❤", "❤ ❤", "❤ ❤ ❤", "❤ ❤ ❤ ❤", "❤ ❤ ❤ ❤ ❤", "❤ ❤ ❤ ❤ ❤ ❤"]

word_list = [
    "apple", "grape", "chair", "python", "castle", "island", "banana",
    "bottle", "awkward", "mystify", "zephyr", "cryptic", "fuchsia", "zephyr", "mystify"
]

lives = 6

random_word = random.choice(word_list)


placeholder = ""
length = len(random_word)
for i in range(length):
    placeholder += "_"
print("Word:", placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    
    display = ""
    correct = False
    for letter in random_word:
        if letter == guess:
            correct = True
            correct_letters.append(guess)
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    
    if not correct:
        lives -= 1
        print("Wrong guess!")

    
    print("Lives:", stages[lives])


    if "_" not in display:
        game_over = True
        print("🎉 You win!")

    if lives == 0:
        game_over = True
        print("💀 You lose! The word was:", random_word)
