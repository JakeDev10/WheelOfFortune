'''
#Wheel of Fortune Pseudocode
#~~~STRUCTURE OF A TURN~~~
#Spin the wheel
#If the wheel selection is Lose a Turn, end the player's turn.
#If the wheel selection is BANKRUPT, reset the player's bank to 0 and end their turn.
#If the wheel selection is a dollar value, they can guess a consonant.
#If they successfully guess a consonant, they earn the dollar value they spun (regardless of # of consonants)
#After a successful guess, they have the opportunity to buy vowels
#After buying vowels or not, they have the opportunity to solve the puzzle.


import random

goalWord = ''
usedWords = empty set
endRound = 0                #flag used on incorrect guesses
round = 0                   #round number
playerTurn = 1              
endTurn = 0
consonants = set of consonants
vowels = set of vowels
vowelCount = 0
wheel = list of money values where 0 is lose a turn and -1 is bankrupt
guesses = empty set
winnings = [0, 0, 0]
tempWinnings = [0, 0, 0]

open words_alpha.txt
load into list called words
close words_alpha.txt

function chooseWord()
    global goalWord

    choose random word
    ensure it is unique, else choose another
    goalWord = random word

function guessConsonant(prize)
    global tempWinnings
    global guesses

    userInput = input "Guess a consonant: "
    ensure input is a consonant, else re-prompt for input

    if userInput in goalWord
        tempWinnings[playerTurn - 1] += prize
        guesses.add(userInput)
        print "Correct!"
        return 1            #allows turn to continue
    else
        print "That's not in the word."
        return 0            #ends player's turn

function guessVowel()
    global guesses
    global vowelCount
    userInput = input "Guess a vowel: "
    ensure input is vowel and not in guesses, else re-prompt

    if userInput in goalWord
        guesses.add(userInput)
        return 1            #allows turn to continue
    else
        return 0            #ends player's turn

function spinWheel()
    choose random element from wheel
    if element == 'special'                         #this is the $10,000 and 2 bankrupt wedge
        roll = choose random range 1-3              #this rolls whether it's $10,000 or bankrupt
            if roll = 3
                return 10000
            else
                return -1                           #this represents bankrupt
    else
        return element

function displayWord()
    displayWord = ''

    for i in range (0, length of goalWord)
        if goalWord[i] in guesses
            add goalWord[i] to displayWord
        else
            add '_' to displayWord

    print "The word so far: {displayWord}"

function guessWord()
    global winnings

    guess = input "Guess the word!"
    ensure input is alpha, else prompt again
    make guess lower

    if guess = goalWord
        print "Congratulations, you got it!"



print """
==============================
        Let's play
W H E E L  O F  F O R T U N E!
==============================
"""
#round 1 main loop
while endRound == 0
    print "Round 1, player {playerTurn}'s turn!"
    displayWord()
    prize = spinWheel()

    if prize = -1
        print "Bankrupt!"
        Zero out current player's tempWinnings
    else if prize = 0
        print "Lose a turn!"
    else                            #The main part of a turn
        print "You rolled {prize}!"
        endTurn = guessConsonant(prize)
        displayWord()
        
        while endTurn = 0           #If they guessed a consonant correctly they can play on
            print menu              #1 to guess vowel, 2 to guess word, 3 to pass
            while validInput = 0
                menuEntry = input "What would you like to do? [1-3]"
                if menuEntry is not in range(1,4)
                    print "Invalid entry, try again"
                else
                    validInput = 1
            if menuEntry = 1 and vowelCount = 5
                print "No more vowels available!"
            else if menuEntry = 1
                endTurn = guessVowel()
            else if menuEntry = 2
                guessWord()
                endTurn = 1
    endTurn = 0
    playerTurn = (playerTurn + 1) mod 3

for i in range(1,4)             
    add tempWinnings[i] to winnings[i]          #bank winnings
tempWinnings = [0,0,0]
playerTurn = 2                                  #starting player rotates
guesses = empty set                             #reset guesses
chooseWord()                                    #reset word

print """
Round 1 over!
Player 1 has {tempWinnings[0]} banked
Player 2 has {tempWinnings[1]} banked
Player 3 has {tempWinnings[2]} banked"""


#round 2
repeat of round 1 code block

for i in range(1,4)             
    add tempWinnings[i] to winnings[i]          #bank winnings
tempWinnings = [0,0,0]
guesses = empty set                             #reset guesses
chooseWord()                                    #reset word

finalPlayer = index + 1 of max winnings
'''