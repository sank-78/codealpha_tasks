# codealpha_tasks
🕹️Hangman Game (Python)
 Goal

A simple text-based Hangman Game where the player tries to guess a randomly chosen word, one letter at a time. The player has 6 chances to make incorrect guesses before the game ends.

 Concepts Used

random — to select a random word

while loop — to keep the game running

if-else statements — to check guesses and game logic

strings and lists — to manage words and guesses

 How to Play

Run the Python script in your terminal or IDE.

The program will display blank spaces for each letter in a hidden word.

Type one letter at a time to guess the word.

You have 6 incorrect attempts — use them wisely!

The game ends when you either guess all the letters or run out of attempts.
Gameplay Instructions
You will see a word represented by underscores (_).

Enter one letter at a time to guess.

If you guess correctly, the letter is revealed in its position.

If you guess incorrectly, you lose one of your 6 attempts.

The game ends when:

You guess all letters correctly (You win 🎉)

You use up all attempts (Game over 😢)

Example Output
text
Welcome to Hangman!
Guess the word. You have 6 incorrect attempts.

_ _ _ _ _ _ 

Guess a letter: a
Good guess!

_ a _ _ _ a _ 

Guess a letter: z
Wrong guess! You have 5 attempts left.

Future Improvements

1-Add difficulty levels (easy, medium, hard)

2-Show used letters on screen

3-Allow replay after finishing one game
