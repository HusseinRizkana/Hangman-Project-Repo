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
- Does what you have built in this milestone connect to the previous one? If so explain how. What technologies are used? Why have you used them? Have you run any commands in the terminal? If so insert them using backticks (To get syntax highlighting for code snippets add the language after the first backticks).

- Example below:

``` 
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181 
```

- The above command is used to check whether the topic has been created successfully, once confirmed the API script is edited to send data to the created kafka topic. The docker container has an attached volume which allows editing of files to persist on the container. The result of this is below:
```
"""Insert your code here"""
```
Insert screenshot of what you have built working.

## Milestone n
---
Continue this process for every milestone, making sure to display clear understanding of each task and the concepts behind them as well as understanding of the technologies used.

Also don't forget to include code snippets and screenshots of the system you are building, it gives proof as well as it being an easy way to evidence your experience!

## Conclusions
---
Maybe write a conclusion to the project, what you understood about it and also how you would improve it or take it further.

Read through your documentation, do you understand everything you've written? Is everything clear and cohesive?