import random

class Hangman:
    def __init__(self, word_list:list[str], num_lives:int=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.list_of_guesses = []
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(set(self.word))
        
    
    def _check_guess(self,guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Unlucky {guess} is not in the word")
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left")
            
    def ask_for_input(self):
        guess =  input("guess a letter:  ")
        if not guess.isalpha():
            print("invalid letter. Please, enter a single alphabetical character")
        elif guess in self.list_of_guesses: 
            print("You already have tried that letter!")
        else:
            self._check_guess(guess)
            self.list_of_guesses.append(guess)
    
def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list=word_list,num_lives=num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(game.word_guessed)
            print(game.word)
            break
        if game.num_letters>0:
            game.ask_for_input()
            
        if game.num_lives>0 and game.num_letters==0:
            print("Congratulations. You won the game")
            print(game.word_guessed)
            print(game.word)
            break
            
    

if __name__=="__main__":
    
    word_list = ["apple","pear","banana","mango","watermelon"]
    play_game(word_list=word_list)
         
            
            