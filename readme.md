# Example Project Documentation Guideline
> This is a terminal hangman game where the user can guess letter by letter from the console the hidden word. After the set number of guesses are used or the word is guessed fully the player loses or wins respectively. This game was developed in python. 

## Milestone 1
---
- A hardcoded list of words is used where a random word from this list is chosen as the subject of the round of this game.

- The Random library is used to choose a word from a given list of words. This is a reliable framework.

```
import random

word_list = ["apple","pear","banana","mango","watermelon"]
word = random.choice(word_list)
```

- a user is prompted to make a guess by inputting a single letter.


## Milestone 2
---
- The user input function which takes in user input and checks its validity returning whether the response or valid or asking for a different response if the response is not valid. 
``` 
ask_for_input()   
```
- For valid responses the function prints whether the letter input is in the hidden word or not.

- Example below:

```
what is your guess?:  a
Good guess! a is in the word.
```
```
what is your guess?:  b
Sorry, b is not in the word. Try again.
```
- For invalid responses the function prints requests a valid response and the user is prompted to input a single alphabetical letter.

- Example below:
```
what is your guess?:  11
invalid letter. Please, enter a single alphabetical character
what is your guess?:  
```




## Milestone 3
---
- Created a class called Hangman(). Inside the class, an init method was created to initialise the attributes of the class to pass in word_list and num_lives as parameters. num_lives defaults to 5.

- attributes of the Hangman() class:
1. word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.

2. word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. If the player guesses 'a', the list would be ['a', '', '', '', ''].

3. num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.

4. num_lives: int - The number of lives the player has at the start of the game.

5. word_list: list - A list of words.

6. list_of_guesses: list - A list of the guesses that have already been tried. Set this to an empty list initially.

- The hangman class has two functions 
```
word_list = ["apple","pear","banana","mango","watermelon"]
hangman = Hangman(word_list=word_list)
hangman.ask_for_input()
```
- the ask_for_input() function is the function running the main loop of the game. The user is prompted to input a letter to make a guess.

```
hangman._check_guess(guess)
```
- the _check_guess() function is an internal function used for checking if the guessed letter is in the hidden word


## Milestone 5
- The Hangman class has been abstracted to
```
word_list = ["apple","pear","banana","mango","watermelon"]

play_game(word_list)
```
- the play_game() function removes the Hangman class boiler-plate for initialising and allows for a smoother user experience. This is done through the default setting of num_lives to 5 and creating a loop the the user to go through with a win and lose scenario.

## Playing the game
- To play the game all the user has to do is run the milestone_5.py python file. This will launch the game in terminal with the given word list of 5 fruits. 
1. A word from the five given fruits will be chosen at random 
2. The user will be prompted to enter a letter in the terminal. 
```
what is your guess?:  
```
3. The user should enter a character and presses enter
4. If the entry is a valid entry (single alphabetical letter) the game will print whether the guess is in the word or not otherwise the user will be prompted to enter another valid guess
5. This repeats until the win condition of the user guessing all the letters of the word or the lose condition of the user running out of lives

## Conclusions
---
- This is a working simple hangman project. This code has only one class defined in milestone_5.py and therefore no further simplification is required.

- Adaptations on this project may include the following:
- Adaptations to the game: keeping score of different rounds to keep track of highscores or adding timed rounds
- Developments to useability: adding in a user interface other than the terminal to aid in the userfriendliness of the game.
- Increasing code maintainability:
  applying unit tests to avoid regressional errors upon further development.