import random

word_list = ["python", "code", "hangman", "alpha", "flask"]

chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)  
guessed_letters = [] 
max_attempts = 6
incorrect_guesses = 0

print("Welcome to Hangman!")
print("Guess the word: ", " ".join(display))

while incorrect_guesses < max_attempts and "_" in display:
    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print(f"Good job! '{guess}' is in the word.")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! '{guess}' is not in the word.")
        print(f"Remaining attempts: {max_attempts - incorrect_guesses}")

    print("Word: ", " ".join(display))
    print("Guessed letters: ", ", ".join(guessed_letters))

if "_" not in display:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)
