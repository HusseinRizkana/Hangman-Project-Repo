import random 
def ask_for_input():
    valid = False
    while not valid:
        guess = input("what is your guess?:  ")
        valid = check_guess(guess)      
    return 

def check_guess(guess):
    if len(guess)==1 and guess.isalpha():
        if guess in word:
            print( f"Good guess! {guess} is in the word.")
            return True
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            return True
    else:
        print("invalid letter. Please, enter a single alphabetical character")
        return False

 
    
if __name__ == "__main__":
    word_list = ["apple","pear","banana","mango","watermelon"]
    word = random.choice(word_list)
    ask_for_input()   
