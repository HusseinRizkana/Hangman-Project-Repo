import random

word_list = ["apple","pear","banana","mango","watermelon"]
word = random.choice(word_list)
guess = input("guess a letter")
if len(guess)==1 and guess.isalpha():
    print("good guess!")
else:
    print("Oops! That is not a valid input.")
