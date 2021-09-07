# Problem Set 2, hangman.py
# Name: Vanessa Santana


# Hangman Game
# -----------------------------------

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


###################################################
# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
###################################################

wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    secret_word_len = len(secret_word)
    letters_matched = 0
    
    for char in secret_word:
        for i in letters_guessed:
            
            if char == i:
                letters_matched += 1
    
    if letters_matched == secret_word_len:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    x = 0

    for char in secret_word:
        x = 0
        for i in letters_guessed:

            if char == i:
                guessed_word += (i + " ")

            else:
                x += 1
                if x == len(letters_guessed):
                    guessed_word += "_ "
                    
                    
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    all_letters = string.ascii_lowercase
    
    available_letters_list = []
    available_letters = ""

    for char in all_letters:
        available_letters_list.append(char)
    
    for char in letters_guessed :
        available_letters_list.remove(char)

    for char in available_letters_list:
        available_letters += char
    

    return available_letters
    
    

def game_introduction(word_length, guessed_word, i, number_guesses, available_letters):
    '''
    word_length: is the length of the secret word.
    guessed_word: is an empty string with an underscore for ech letter in the secret word.
    i: is currently zero (it is the variable used in creating the guessed word with all underscores).
    number_guesses: the initial number of guesses in the game, 6.
    available_letters: starts with all the letters in the alphabet (in lowercase).
    

    Returns
    -------
    None.

    '''
  
    print()
    print()
    print("Welcome to the game of Hangman!")
    print("I am thinking of a word that is " + str(word_length ) + " letters long:")
    
    # while i <= word_length:
    while i < word_length:    
        guessed_word += "_ "
        i += 1
    # guessed_word = get_guessed_word(secret_word, letters_guessed)
    
    print()
    print()
    print(guessed_word)
    print()
    print("You have " + str(number_guesses) + " guesses left.")
    print("Available letters: " + available_letters)
    
    print()
    print("Please note: You get 3 initial warnings in case you enter")
    print("symbols, numbers, or a letter that is no longer available.")
    
    print()
    print("After 3 warnings, your number of guesses will be affected.")

    
    
def validate_input(letter_guessed, repeated_guess, available_letters):
    '''
    letter_guessed: the character just enterd by the user.
    repeated_guess: list of unique valid lowercase letters that have already been guessed.
    available_letters: string of letters that have not been guessed yet.

    Returns
    -------
    valid_input: True if input is one character long, is not a repeated guess, and not a number or a symbol.

    '''
    valid_input = True
    # invalid_input_reason = ""
    letter_guessed_toLower = ""
    
    
    
    if len(letter_guessed) != 1: #CHECK - if the input is NOT 1 letter
        valid_input = False
        # invalid_input_reason = "Invalid input! You entered more than one character."
        
        print()
        print("Invalid input! You entered more than one character.")
        print()
        print("##########")
        print("GAME RULE: Please enter one letter at a time.")
        print("##########")
        print()
        return valid_input
    
    else: #The letter input IS 1 character
    
        if (letter_guessed.islower != True): #CHECK - if the input is NOT lowercase
        
            letter_guessed_toLower = letter_guessed.lower()
            
            if (letter_guessed_toLower.isalpha() == False): #CHECK - if the input is NOT a letter
            
                if (letter_guessed.isdigit() == True): #CHECK if input is a number
                    valid_input = False
                    print()
                    print("Invalid input! You entered '" + letter_guessed + "', a digit value.")
                    print()
                    print("##########")
                    print("GAME RULE: Please enter letter values only.")
                    print("##########")
                    print()
                    return valid_input
                
                else: #(letter_guessed.isalnum() == False): #CHECK if input is a symbol
                    valid_input = False
                    print()
                    print("Invalid input! You entered '" + letter_guessed + "', a symbol value.")
                    print()
                    print("##########")
                    print("GAME RULE: Please enter letter values only.")
                    print("##########")
                    print()
                    return valid_input
                
            
            else: 
                
                if (letter_guessed_toLower in repeated_guess): #CHECK - if the lowercase input is a repeated guess
                    valid_input = False
                    # invalid_input_reason = "Invalid input! You already guessed the letter '" + str(letter_guessed) + "'."
                    
                    print()
                    print("Invalid input! You already guessed the letter '" + str(letter_guessed) + "'.")
                    print()
                    print("##########")
                    print("GAME RULE: Please enter a letter from the list of available letters left.")
                    print("##########")
                    print()
                    # print("Available letters: " + available_letters)
                    print()
                    return valid_input
                
                else: #letter_guessed_toLower is NOT a repeated guess
                    return valid_input
                
                
        else:
            
             if (letter_guessed in repeated_guess): #CHECK - if the already lowercase input is a repeated guess
                valid_input = False
                # invalid_input_reason = "Invalid input! You already guessed the letter '" + str(letter_guessed) + "'."
                
                print()
                print("Invalid input! You already guessed the letter '" + str(letter_guessed) + "'.")
                print()
                print("##########")
                print("GAME RULE: Please enter a letter from the list of available letters left.")
                print("##########")
                print("Available letters: " + available_letters)
                print()
                return valid_input
            
             else: #letter_guessed was a lowercase letter, and is NOT a repeated guess
                return valid_input

    
    
def letter_matched(guessed_letter, secret_word):
    '''
    guessed_letter: letter guessed.
    secret_word: string, the word the user is guessing in the current Hangman game.
    returns: boolean, True if letter is in secret word, False if letter is not in
    secret word.
    '''
    match = False
    
    for char in secret_word:
        if char == guessed_letter:
            match = True
            break
        
    print()
         
    if match:
        print()
        print("Good guess! The letter '" + guessed_letter + "' is in my word.")
        print()
        return True
    else:
        print()
        print("Oops! The letter '" + guessed_letter + "' is not in my word.")
        print()
        return False

    
    
def guessed_letter_penalty(is_valid_input, letter_guessed, match, guessed_word, number_guesses, available_letters, word_guessed):
    '''
    is_valid_input: True if input is one character long, is not a repeated guess, and not a number or a symbol; False otherwise.
    letter_guessed: the character just enterd by the user.
    match: returns True if the letter guessed matches a letter in the the secret word.
    guessed_word: returns a string of underscores and the letters that have been matched in the secret word so far.
    number_guesses: initially 6 (at the start of the game), but if have guessed wrong, the value will decrease depending on the penalty.
    available_letters: string of letters that are available to guess from.
    warning: initially 3 (at the start of the game), but the value will decrease if invalid input continues to be entered.
        
    Returns
    -------
    Number of guesses left
    
    '''
    
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    penalty_amount = -1
    global warning

    
    if (letter_guessed == "*"):
        ##DO NOTHING##
        print()
        
    elif (is_valid_input): #VALID INPUT
    
        if (match == False):
            
            # penalty_amount = 0
            # number_guesses -= penalty_amount
            
            if (letter_guessed in consonants) or (letter_guessed == ''):
                penalty_amount = 1
                number_guesses -= penalty_amount
                
            else: #(letter_guessed in vowels):
                penalty_amount = 2
                number_guesses -= penalty_amount
            
            if (penalty_amount == 1):
                print()
                print("you just lost " + str(penalty_amount) + " guess.")
                print()
            else:
                print()
                print("you just lost " + str(penalty_amount) + " guesses.")
                print("(Vowels are worth two guesses)")
                print()
            
        
        
    else: #INVALID INPUT (is_valid_input == False)

        if (warning > 0):
            warning -= 1
            
            # print()
            print("Oh Oh! You just lost a warning.")
            
            if (warning == 1):
                print()
                print("You have " + str(warning) + " warning left.")
                print()
            elif (warning == 0):
                print()
                print("CAUTION: You have " + str(warning) + " warnings left! On your next")
                print("invalid input entered, your guesses remaining will be impacted.")
                print()
            else:
                # print("warning value is: " + str(warning))
                print("You have " + str(warning) + " warnings left.")
                print()
    
            
        else: #warning < 0
            

            print()
            print("You have no more warnings left.")

            if (letter_guessed in consonants) or (letter_guessed == ''):
                penalty_amount = 1
                number_guesses -= penalty_amount
                
            else: #(letter_guessed in vowels):
                penalty_amount = 2
                number_guesses -= penalty_amount
                
            print()
            print("Because you have already entered 3 invalid inputs,")
            
            if (penalty_amount == 1):
                print("you just lost " + str(penalty_amount) + " guess.")
            else:
                print("you just lost " + str(penalty_amount) + " guesses.")
        

    print()
    print(guessed_word)
    print()
    print()
    
    
    # if (word_guessed != True):
    if (word_guessed != True and number_guesses > 0):
        if (number_guesses == 1):
            print("You have " + str(number_guesses) + " guess left.")
        else:
            print("You have " + str(number_guesses) + " guesses left.")
            
        print("You have the following letters available: " + available_letters)
        
    elif (word_guessed != True and number_guesses <= 0):
        print("You have 0 guesses left.")
        number_guesses = 0

    return number_guesses

    
    
def total_score(number_guesses, secret_word, word_guessed):
    '''
    number_guesses: the number of guesses remaining.
    secret_word: the secret word.
    word_guessed: is True if all the letters guessed so far match 
    the secret word, and is False if not.
    returns: None
    '''
    
    # individual_count = 0
    individual_count_list = []
    score = 0
    
    for char in secret_word:
        if (char not in individual_count_list):
            individual_count_list.append(char)
            # individual_count += 1
    
    
    score = number_guesses * len(individual_count_list)
    
    
    if (word_guessed):
        print()
        print("Congratulations, you won this Hangman game! You guessed all")
        print("the letters in the word with a remaining letter guess balance of: " + str(number_guesses) + ".")
        print()
        print()
        print("You won the game with a total score of: " + str(score) + ".")
    else:
        print()
        print("Sorry! You lost this Hanglman game.")
        print("You ran out of guesses!")
        print()
        print("You did not guess the letters in the word.")
        print("Your score was : " + str(score) + ".")
        print()
    
    # print("The number of unique letters in the word: " + str(len(individual_count_list)))

    
    
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    secret_word = choose_word(wordlist)
    # print(secret_word)
    
    ##############################TEST - START
    # secret_word = "tact"
    # secret_word = "else"
    
    ##############################TEST - END
    
    
    ##############################VARIABLES - START
    
    #GAME INTRO FUNCTION VARIABLES
    word_length = len(secret_word)
    guessed_word = ""
    i = 0
    number_guesses = 6
    all_letters = string.ascii_lowercase
    available_letters = all_letters
    #GAME INTRO FUNCTION VARIABLES
    
    
    letter_guessed = ""
    letters_guessed = []
    word_guessed = False
    
    global warning 
    warning = 3
    
    repeated_guess = []
    
    # score = 0
    # vowels = ['a', 'e', 'i', 'o', 'u']
    
    is_valid_input = False
    # penalty = -1
    
    game_round = 0

    ##############################VARIABLES - END


    
    game_introduction(word_length, guessed_word, i, number_guesses, available_letters)  

    
    while (word_guessed != True and number_guesses > 0):
        
        print()
        game_round += 1
        match = False
        
        
        letter_guessed = input("Please guess a letter: ")
        
        print()
        print()
        print("----------------- HANGMAN ROUND " + str(game_round) + " - '" + letter_guessed + "' -----------------")
        
        is_valid_input = validate_input(letter_guessed, repeated_guess, available_letters)
        
                    
        # print()
        # print()
        # print("----------------- HANGMAN ROUND " + str(game_round) + " - '" + letter_guessed + "' -----------------")
        
        
        if (is_valid_input): #Input is 1 character, a letter, and is not a repeated guess
    
                
            letter_guessed = letter_guessed.lower()
            letters_guessed.append(letter_guessed)
            
            match = letter_matched(letter_guessed, secret_word)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            
            available_letters = get_available_letters(letters_guessed)
            word_guessed = is_word_guessed(secret_word, letters_guessed)
            
            
            ###################PENALTY
            number_guesses  = guessed_letter_penalty(is_valid_input, letter_guessed, match, guessed_word, number_guesses, available_letters, word_guessed)
            ###################PENALTY

            repeated_guess.append(letter_guessed)
            
        else: #is_valid_input == False
            
            match = False
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            
            available_letters = get_available_letters(letters_guessed)
            word_guessed = is_word_guessed(secret_word, letters_guessed)
            
            ###################PENALTY
            number_guesses  = guessed_letter_penalty(is_valid_input, letter_guessed, match, guessed_word, number_guesses, available_letters, word_guessed)
            ###################PENALTY
                
    
    
    ######### GAME ENDED #########
    print()
    print("This Hangman game has ended!")
    print()
    
    total_score(number_guesses, secret_word, word_guessed)
    
    print()
    print("The word was: '" + secret_word + "'.")
    print()
    print()
    print("----------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------- END OF HANGMAN GAME ----------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------")
    ######### GAME ENDED #########



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def removeSpaces(word):
    newWord = ''
    for char in word:
        if char != ' ':
            newWord = newWord + char
            
    return newWord



def wordlist_length_dictionary(wordlist):
    wordlist_lendict = {}
    
    wordlist_len = len(wordlist)
    word_len = 0
    
    
    for i in range(wordlist_len):
        word_len = len(wordlist[i])
        
        if (word_len not in wordlist_lendict):
            wordlist_lendict[word_len] = []

        wordlist_lendict[word_len].append(wordlist[i])
    
    # print(wordlist_lendict)
    return wordlist_lendict  



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    letters_match = True
    
    my_word = removeSpaces(my_word)
    my_word_length = len(my_word)
    
    other_word_len = len(other_word)
    
    if (my_word_length == other_word_len):
        for i in range(my_word_length):
            if (my_word[i] != "_"):
                if (my_word[i] != other_word[i]):
                    letters_match = False
            else:
                if (my_word.count(other_word[i]) > 0):
                    letters_match = False
        
    else:
        letters_match = False 
    
    return letters_match



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word = removeSpaces(my_word)
    my_word_len = len(my_word)
    
    wordlist_dictionary = wordlist_length_dictionary(wordlist)
    length_list = wordlist_dictionary[my_word_len]
    
    my_word_matches = ""
    
    for word in length_list:
        word_match = match_with_gaps(my_word, word)
        
        # for i in range(my_word_len):
            
        #     if (my_word[i] != "_"):
        #         if (my_word[i] != word[i]):
        #             word_match = False
             
        #     else: #(my_word[i] == "_"):
        #         if (my_word.count(word[i]) > 0):
        #             word_match = False
        
        
        if (word_match == True):
            my_word_matches = my_word_matches + word + " "
    
    return my_word_matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''

    secret_word = choose_word(wordlist)
    # print(secret_word)
    
    ##############################TEST - START
    # secret_word = "tact"
    # secret_word = "else"
    # secret_word = "apple"
    
    ##############################TEST - END
    
    
    ##############################VARIABLES - START
    
    #GAME INTRO FUNCTION VARIABLES
    word_length = len(secret_word)
    guessed_word = ""
    i = 0
    number_guesses = 6
    all_letters = string.ascii_lowercase
    available_letters = all_letters
    #GAME INTRO FUNCTION VARIABLES
    
    
    letter_guessed = ""
    letters_guessed = []
    word_guessed = False
    
    global warning 
    warning = 3
    
    repeated_guess = []
    
    # score = 0
    # vowels = ['a', 'e', 'i', 'o', 'u']
    
    is_valid_input = False
    # penalty = -1
    
    game_round = 0

    ##############################VARIABLES - END


    
    game_introduction(word_length, guessed_word, i, number_guesses, available_letters)  

    
    while (word_guessed != True and number_guesses > 0):
        
        print()
        game_round += 1
        match = False
        
        
        letter_guessed = input("Please guess a letter: ")
        
        print()
        print()
        print("----------------- HANGMAN ROUND " + str(game_round) + " - '" + letter_guessed + "' -----------------")
        
        if (letter_guessed != "*"):
        
            is_valid_input = validate_input(letter_guessed, repeated_guess, available_letters)
            
                        
            # print()
            # print()
            # print("----------------- HANGMAN ROUND " + str(game_round) + " - '" + letter_guessed + "' -----------------")
            
            
            if (is_valid_input): #Input is 1 character, a letter, and is not a repeated guess
        
                    
                letter_guessed = letter_guessed.lower()
                letters_guessed.append(letter_guessed)
                
                match = letter_matched(letter_guessed, secret_word)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                
                available_letters = get_available_letters(letters_guessed)
                word_guessed = is_word_guessed(secret_word, letters_guessed)
                
                
                ###################PENALTY
                number_guesses  = guessed_letter_penalty(is_valid_input, letter_guessed, match, guessed_word, number_guesses, available_letters, word_guessed)
                ###################PENALTY
    
                repeated_guess.append(letter_guessed)
                
            else: #is_valid_input == False
                
                match = False
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                
                available_letters = get_available_letters(letters_guessed)
                word_guessed = is_word_guessed(secret_word, letters_guessed)
                
                ###################PENALTY
                number_guesses  = guessed_letter_penalty(is_valid_input, letter_guessed, match, guessed_word, number_guesses, available_letters, word_guessed)
                ###################PENALTY
                
        else:
            
            if (number_guesses > 3):
                print()
                print("Please try this option again once your number of guesses is lower.")
                print()
                
            else:
            
                word_guessed_matches = ""
                word_guessed_matches = show_possible_matches(guessed_word)
                
                if(word_guessed_matches == ""):
                    print()
                    print("No matches found for guessed word " + word_guessed + ".")
                    print()
                else:
                    print()
                    print("Possible word matches are:")
                    print(word_guessed_matches)
                    print()
                
                

            
            match = False
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            
            available_letters = get_available_letters(letters_guessed)
            word_guessed = is_word_guessed(secret_word, letters_guessed)
            
            ###################PENALTY
            number_guesses  = guessed_letter_penalty(is_valid_input, letter_guessed, match, guessed_word, number_guesses, available_letters, word_guessed)
            ###################PENALTY
            

    
    
    ######### GAME ENDED #########
    print()
    print("This Hangman game has ended!")
    print()
    
    total_score(number_guesses, secret_word, word_guessed)
    
    print()
    print("The word was: '" + secret_word + "'.")
    print()
    print()
    print("----------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------- END OF HANGMAN GAME ----------------------------------------------")
    print("----------------------------------------------------------------------------------------------------------------")
    ######### GAME ENDED #########



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    
    
    

############### SAMPLE OUTPUT - hangman (WINNING GAME) - START
# Loading word list from file...
#    55900 words loaded.


# Welcome to the game of Hangman!
# I am thinking of a word that is 4 letters long:


# _ _ _ _ 

# You have 6 guesses left.
# Available letters: abcdefghijklmnopqrstuvwxyz

# Please note: You get 3 initial warnings in case you enter
# symbols, numbers, or a letter that is no longer available.

# After 3 warnings, your number of guesses will be affected.


# Please guess a letter: a


# ----------------- HANGMAN ROUND 1 - 'a' -----------------


# Good guess! The letter 'a' is in my word.


# _ a _ _ 


# You have 6 guesses left.
# You have the following letters available: bcdefghijklmnopqrstuvwxyz


# Please guess a letter: a


# ----------------- HANGMAN ROUND 2 - 'a' -----------------

# Invalid input! You already guessed the letter 'a'.

# ##########
# GAME RULE: Please enter a letter from the list of available letters left.
# ##########


# Oh Oh! You just lost a warning.
# You have 2 warnings left.


# _ a _ _ 


# You have 6 guesses left.
# You have the following letters available: bcdefghijklmnopqrstuvwxyz


# Please guess a letter: s


# ----------------- HANGMAN ROUND 3 - 's' -----------------


# Oops! The letter 's' is not in my word.


# you just lost 1 guess.


# _ a _ _ 


# You have 5 guesses left.
# You have the following letters available: bcdefghijklmnopqrtuvwxyz


# Please guess a letter: $


# ----------------- HANGMAN ROUND 4 - '$' -----------------

# Invalid input! You entered '$', a symbol value.

# ##########
# GAME RULE: Please enter letter values only.
# ##########

# Oh Oh! You just lost a warning.

# You have 1 warning left.


# _ a _ _ 


# You have 5 guesses left.
# You have the following letters available: bcdefghijklmnopqrtuvwxyz


# Please guess a letter: t


# ----------------- HANGMAN ROUND 5 - 't' -----------------


# Good guess! The letter 't' is in my word.


# t a _ t 


# You have 5 guesses left.
# You have the following letters available: bcdefghijklmnopqruvwxyz


# Please guess a letter: E


# ----------------- HANGMAN ROUND 6 - 'E' -----------------


# Oops! The letter 'e' is not in my word.


# you just lost 2 guesses.
# (Vowels are worth two guesses)


# t a _ t 


# You have 3 guesses left.
# You have the following letters available: bcdfghijklmnopqruvwxyz


# Please guess a letter: e


# ----------------- HANGMAN ROUND 7 - 'e' -----------------

# Invalid input! You already guessed the letter 'e'.

# ##########
# GAME RULE: Please enter a letter from the list of available letters left.
# ##########


# Oh Oh! You just lost a warning.

# CAUTION: You have 0 warnings left! On your next
# invalid input entered, your guesses remaining will be impacted.


# t a _ t 


# You have 3 guesses left.
# You have the following letters available: bcdfghijklmnopqruvwxyz


# Please guess a letter: e


# ----------------- HANGMAN ROUND 8 - 'e' -----------------

# Invalid input! You already guessed the letter 'e'.

# ##########
# GAME RULE: Please enter a letter from the list of available letters left.
# ##########



# You have no more warnings left.

# Because you have already entered 3 invalid inputs,
# you just lost 2 guesses.

# t a _ t 


# You have 1 guess left.
# You have the following letters available: bcdfghijklmnopqruvwxyz


# Please guess a letter: c


# ----------------- HANGMAN ROUND 9 - 'c' -----------------


# Good guess! The letter 'c' is in my word.


# t a c t 



# This Hangman game has ended!


# Congratulations, you won this Hangman game! You guessed all
# the letters in the word with a remaining letter guess balance of: 1.


# You won the game with a total score of: 3.

# The word was: 'tact'.


# ----------------------------------------------------------------------------------------------------------------
# --------------------------------------------- END OF HANGMAN GAME ----------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
############### SAMPLE OUTPUT - hangman (WINNING GAME) - END



############### SAMPLE OUTPUT - hangman (LOSING GAME) - START
# Loading word list from file...
#    55900 words loaded.


# Welcome to the game of Hangman!
# I am thinking of a word that is 4 letters long:


# _ _ _ _ 

# You have 6 guesses left.
# Available letters: abcdefghijklmnopqrstuvwxyz

# Please note: You get 3 initial warnings in case you enter
# symbols, numbers, or a letter that is no longer available.

# After 3 warnings, your number of guesses will be affected.


# Please guess a letter: a


# ----------------- HANGMAN ROUND 1 - 'a' -----------------


# Oops! The letter 'a' is not in my word.


# you just lost 2 guesses.
# (Vowels are worth two guesses)


# _ _ _ _ 


# You have 4 guesses left.
# You have the following letters available: bcdefghijklmnopqrstuvwxyz


# Please guess a letter: b


# ----------------- HANGMAN ROUND 2 - 'b' -----------------


# Oops! The letter 'b' is not in my word.


# you just lost 1 guess.


# _ _ _ _ 


# You have 3 guesses left.
# You have the following letters available: cdefghijklmnopqrstuvwxyz


# Please guess a letter: c


# ----------------- HANGMAN ROUND 3 - 'c' -----------------


# Oops! The letter 'c' is not in my word.


# you just lost 1 guess.


# _ _ _ _ 


# You have 2 guesses left.
# You have the following letters available: defghijklmnopqrstuvwxyz


# Please guess a letter: 2


# ----------------- HANGMAN ROUND 4 - '2' -----------------

# Invalid input! You entered '2', a digit value.

# ##########
# GAME RULE: Please enter letter values only.
# ##########

# Oh Oh! You just lost a warning.
# You have 2 warnings left.


# _ _ _ _ 


# You have 2 guesses left.
# You have the following letters available: defghijklmnopqrstuvwxyz


# Please guess a letter: d


# ----------------- HANGMAN ROUND 5 - 'd' -----------------


# Oops! The letter 'd' is not in my word.


# you just lost 1 guess.


# _ _ _ _ 


# You have 1 guess left.
# You have the following letters available: efghijklmnopqrstuvwxyz


# Please guess a letter: e


# ----------------- HANGMAN ROUND 6 - 'e' -----------------


# Good guess! The letter 'e' is in my word.


# e _ _ e 


# You have 1 guess left.
# You have the following letters available: fghijklmnopqrstuvwxyz


# Please guess a letter: f


# ----------------- HANGMAN ROUND 7 - 'f' -----------------


# Oops! The letter 'f' is not in my word.


# you just lost 1 guess.


# e _ _ e 


# You have 0 guesses left.
# You have the following letters available: ghijklmnopqrstuvwxyz

# This Hangman game has ended!


# Sorry! You lost this Hanglman game.
# You ran out of guesses!

# You did not guess the letters in the word.
# Your score was : 0.


# The word was: 'else'.


# ----------------------------------------------------------------------------------------------------------------
# --------------------------------------------- END OF HANGMAN GAME ----------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
############### SAMPLE OUTPUT - hangman (LOSING GAME) - END



############### SAMPLE OUTPUT - hangman_with_hints (WINNING GAME) - START
# Loading word list from file...
#    55900 words loaded.


# Welcome to the game of Hangman!
# I am thinking of a word that is 5 letters long:


# _ _ _ _ _ 

# You have 6 guesses left.
# Available letters: abcdefghijklmnopqrstuvwxyz

# Please note: You get 3 initial warnings in case you enter
# symbols, numbers, or a letter that is no longer available.

# After 3 warnings, your number of guesses will be affected.


# Please guess a letter: a


# ----------------- HANGMAN ROUND 1 - 'a' -----------------


# Good guess! The letter 'a' is in my word.


# a _ _ _ _ 


# You have 6 guesses left.
# You have the following letters available: bcdefghijklmnopqrstuvwxyz


# Please guess a letter: l


# ----------------- HANGMAN ROUND 2 - 'l' -----------------


# Good guess! The letter 'l' is in my word.


# a _ _ l _ 


# You have 6 guesses left.
# You have the following letters available: bcdefghijkmnopqrstuvwxyz


# Please guess a letter: *


# ----------------- HANGMAN ROUND 3 - '*' -----------------

# Possible word matches are:
# addle adult agile aisle amble ample amply amyls angle ankle apple apply aptly arils atilt 



# a _ _ l _ 


# You have 6 guesses left.
# You have the following letters available: bcdefghijkmnopqrstuvwxyz


# Please guess a letter: e


# ----------------- HANGMAN ROUND 4 - 'e' -----------------


# Good guess! The letter 'e' is in my word.


# a _ _ l e 


# You have 6 guesses left.
# You have the following letters available: bcdfghijkmnopqrstuvwxyz


# Please guess a letter: *


# ----------------- HANGMAN ROUND 5 - '*' -----------------

# Possible word matches are:
# addle agile aisle amble ample angle ankle apple 



# a _ _ l e 


# You have 6 guesses left.
# You have the following letters available: bcdfghijkmnopqrstuvwxyz


# Please guess a letter: D


# ----------------- HANGMAN ROUND 6 - 'D' -----------------


# Oops! The letter 'd' is not in my word.


# you just lost 1 guess.


# a _ _ l e 


# You have 5 guesses left.
# You have the following letters available: bcfghijkmnopqrstuvwxyz


# Please guess a letter: !


# ----------------- HANGMAN ROUND 7 - '!' -----------------

# Invalid input! You entered '!', a symbol value.

# ##########
# GAME RULE: Please enter letter values only.
# ##########

# Oh Oh! You just lost a warning.
# You have 2 warnings left.


# a _ _ l e 


# You have 5 guesses left.
# You have the following letters available: bcfghijkmnopqrstuvwxyz


# Please guess a letter: *


# ----------------- HANGMAN ROUND 8 - '*' -----------------

# Possible word matches are:
# addle agile aisle amble ample angle ankle apple 



# a _ _ l e 


# You have 5 guesses left.
# You have the following letters available: bcfghijkmnopqrstuvwxyz


# Please guess a letter: P


# ----------------- HANGMAN ROUND 9 - 'P' -----------------


# Good guess! The letter 'p' is in my word.


# a p p l e 



# This Hangman game has ended!


# Congratulations, you won this Hangman game! You guessed all
# the letters in the word with a remaining letter guess balance of: 5.


# You won the game with a total score of: 20.

# The word was: 'apple'.


# ----------------------------------------------------------------------------------------------------------------
# --------------------------------------------- END OF HANGMAN GAME ----------------------------------------------
# ----------------------------------------------------------------------------------------------------------------
############### SAMPLE OUTPUT - hangman_with_hints (WINNING GAME) - END





