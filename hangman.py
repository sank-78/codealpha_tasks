import random

# Predefined list of words
words = ["python", "computer", "science", "program", "hangman"]

# Randomly choose one word
word_to_guess = random.choice(words)
guessed_letters = []  
attempts = 6  

print("🎯 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")


while attempts > 0:
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    print("\nWord:", display_word)

    
    if display_word == word_to_guess:
        print("🎉 Congratulations! You guessed the word correctly:", word_to_guess)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.")
        continue

    
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    # Check guess
    if guess in word_to_guess:
        print("✅ Good guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong guess!")
        attempts -= 1
        print(f"Attempts left: {attempts}")

# If player runs out of attempts
if attempts == 0:
    print("\n😢 Game Over! The word was:", word_to_guess)
