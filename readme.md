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




## Milestone n
---
Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions
---
Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?