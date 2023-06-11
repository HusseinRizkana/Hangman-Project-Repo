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
## Conclusions
---
This is a working simple hangman project. This code has only one class in milestone_4.py and therefore no further simplification is required.

Adaptations on this project my include keeping score of different rounds, having times rounds and perhaps adding in a user interface other than the terminal to aid in the userfriendliness of the game.