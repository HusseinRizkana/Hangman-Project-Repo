import random

class Hangman:
    '''
    This class encapsulates the functionality of a hangman game 
    Attributes
        ----------
        word_list : list[str]
            List of available words for the hangman game
        num_lives : int, default 5
            number of lives available to start the game
        word : str
            Word chosen at random from word_list
        list_of_guesses : list[str]
            list of letters guessed thus far
        word_guessed : list[str]
            word unpacked into a list with the unguessed letters filled in with a _
        num_letters : int
            number of remaining unique letters required to guess to guess the full word
    '''
    def __init__(self, word_list:list[str], num_lives:int=5):
        """
        initialises hangman class and its attributes
        Parameters
        ----------
        word_list : list[str]
            List of available words for the hangman game
        num_lives : int, default 5
            number of lives available to start the game

        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list) 
        self.list_of_guesses = []
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(set(self.word))
        
    
    def _check_guess(self,guess):
        """
        checks if the guessed letter is in the word
        Parameters
        ----------
        guess : str,
            single letter input
        """
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for i in range(len(self.word)):
                # add the letter in the appropriate place instead of the "_" 
                # in the word_guess amd decrement the number of letters 
                # remaining to guess num_letters
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            #if guess is not in the word inform user and decrease number of 
            #available lives
            print(f"Unlucky {guess} is not in the word")
            self.num_lives -=1
            print(f"You have {self.num_lives} lives left")
            
    def ask_for_input(self):
        """
        Main loop of game asks user for input and checks if the input 
        is valid or in the word then adjusts hangman attributes accordingly
        """
        guess =  input("guess a letter:  ")
    
        #check that the guess is a single alphabetical letter and inform user if
        #otherwise
        if not guess.isalpha() or len(guess)!=1:
            print("invalid letter. Please, enter a single alphabetical character")
        # if valid input check if it is a repeat guess
        elif guess in self.list_of_guesses: 
            print("You already have tried that letter!")
        else:
        # if input is a valid new guess check if the letter is in the word
            self._check_guess(guess)
            self.list_of_guesses.append(guess)
    
def play_game(word_list):
    """
    main loop to run through hangman game removing initialisation boilerplate
    
    Parameters
    ----------
    word_list : list[str],
        list of words to be used in hangman game words can only contain alphabeticl letters
    """
    #initialise hangman class and number of lives
    num_lives = 5
    game = Hangman(word_list=word_list,num_lives=num_lives)
    while True:
        # lose scenario if user runs out of lives
        # informss them of their loss and ends the game
        if game.num_lives == 0:
            print("You lost!")
            print(game.word_guessed)
            print(game.word)
            break
        # game running scenario asks for user input (main game loop)
        if game.num_letters>0:
            game.ask_for_input()
            
        # win scenario where user has lives remaining and has guessed
        # all the words letters, informs them of their win and the word
        # ends the game
        if game.num_lives>0 and game.num_letters==0:
            print("Congratulations. You won the game")
            print(game.word_guessed)
            print(game.word)
            break
            
    

if __name__=="__main__":
    
    word_list = ["apple","pear","banana","mango","watermelon"]
    play_game(word_list=word_list)
         
            
            