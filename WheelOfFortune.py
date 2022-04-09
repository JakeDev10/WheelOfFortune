#~~~STRUCTURE OF A TURN~~~
#Spin the wheel
#If the wheel selection is a dollar value, they can guess a consonant.
#If they successfully guess a consonant, they earn the dollar value they spun (regardless of # of consonants)
#After a successful guess, they have the opportunity to buy vowels
#After buying vowels or not, they have the opportunity to solve the puzzle.


import random

goalWord = ''
usedWords = set()
guesses = set()             #stores letters guessed
endRound = 0                #flag used on incorrect guesses
round = 1                   #round number
playerTurn = 0             
endTurn = 0
consonants = ('b','c','d','f','g','h','j','k','l','m','n','p',
'q','r','s','t','v','w','x','y','z')
vowels = ('a','e','i','o','u')
vowelCount = 0
wheel = [-1,600,400,300,0,800,350,450,700,300,600,2500,300,600,
'special',500,800,550,400,300,900,500,300,900]              #0 is lose a turn and -1 is bankrupt
winnings = [0, 0, 0]
tempWinnings = [0, 0, 0]

file = open('words_alpha.txt')
words = file.read().splitlines()        #stores dictionary file in words
file.close()

#assigns a random word to goalWord, prevents duplicates
def chooseWord():                       
    global goalWord
    global usedWords

    usedWords.add(goalWord)

    while goalWord in usedWords:
        goalWord = words[random.randrange(0, 370103)]       #there are 370103 words

#gets consonant input, adds to guesses, adjusts tempWinnings
def guessConsonant(prize):
    global tempWinnings
    global guesses
    validInput = 0

    while validInput == 0:                  #input validation
        userInput = input("Guess a consonant: ")
        if userInput in guesses:
            print("That was already guessed, try again")
        elif userInput in consonants:
            validInput = 1
        else:
            print("That's not a lowercase consonant, try again.")

    if userInput in goalWord:
        tempWinnings[playerTurn - 1] += prize
        guesses.add(userInput)
        print("Correct!")
        return 0                            #allows turn to continue
    else:
        print("That's not in the word.")
        return 1                            #ends player's turn

#gets vowel input, adds to guesses, adjusts tempWinnings
def guessVowel():
    global guesses
    global vowelCount
    validInput = 0

    while validInput == 0:                  #input validation
        userInput = input("Guess a vowel: ")
        if userInput in guesses:
            print("That was already guessed, try again")
        elif userInput in vowels:
            validInput = 1
            vowelCount += 1
        else:
            print("That's not a lowercase vowel, try again.")

    if userInput in goalWord:
        guesses.add(userInput)
        displayWord()
        return 0                            #allows turn to continue
    else:
        print("That's not in the word.")
        return 1                            #ends player's turn

#randomly selects a wedge with 1/24 probability, returns prize value
def spinWheel():
    global wedge

    wedge = random.choice(wheel)
    if wedge == 'special':                  #this is the $10,000 and 2 bankrupt wedge
        roll = random.choice(range(1,4))    #this rolls whether it's $10,000 or bankrupt
        if roll == 3:
            return 10000
        else:
            return -1                       #this represents bankrupt
    else:
        return wedge

#prints word in progress based on guesses
def displayWord():                              
    displayWord = ''

    for i in range(0, len(goalWord)):
        if goalWord[i] in guesses:
            displayWord += goalWord[i]
        else:
            displayWord += '_'

    print(f"The word so far: {displayWord}")

#The player tries to solve the game. If successful, sets up for next round
def guessWord():
    global winnings
    global round
    global playerTurn
    global tempWinnings
    global guesses

    validInput = 0

    while validInput == 0:
        guess = input("Guess the word! ")
        if guess.isalpha():
            validInput = 1
        else:
            print("Letters only, please.")
            
    if guess.lower() == goalWord:
        print("Congratulations, you got it!")

        winnings[playerTurn - 1] += tempWinnings[playerTurn - 1]        #set up next round
        tempWinnings = [0, 0, 0]
        guesses = ()
        chooseWord()
        round += 1
        playerTurn = 1              #round 2 starts with player 2
        #DEBUGGING
        print(f"""Winnings so far:
        Player 1: {winnings[0]}
        Player 2: {winnings[1]}
        Player 3: {winnings[2]}""")
    else:
        print("That's not the word.")


print("""
================================
          Let's play
W H E E L   O F   F O R T U N E!
================================
""")

chooseWord()
#round 1 and 2 main loop
while round < 3:
    playerTurn = playerTurn % 3 + 1       #increments player turn by 1, wrapping at 3
    print(f"Round {round}, player {playerTurn}'s turn!")
    print(f"CHEATING the word is {goalWord}")
    displayWord()
    prize = spinWheel()
    validInput = 0

    if prize == -1:
        print("Bankrupt!")
        tempWinnings[playerTurn - 1] = 0
    elif prize == 0:
        print("Lose a turn!")
    else:                            #The main part of a turn
        print(f"You rolled {prize}!")
        endTurn = guessConsonant(prize)     #ends turn if consonant guess is wrong
        displayWord()
        
        while endTurn == 0:           #If they guessed a consonant correctly they can play on
            print(f'''Player {playerTurn}, what do you want to do?
            1. Guess a vowel
            2. Guess the word
            3. Pass your turn''')   
            
            while validInput == 0:      #input validation
                menuEntry = input("What would you like to do? [1-3] ")
                if menuEntry not in ['1','2','3']:
                    print("Invalid entry, try again")
                else:
                    validInput = 1
            validInput = 0

            if menuEntry == '1' and tempWinnings[playerTurn - 1] < 250:
                print("You can't afford a vowel!")
            elif menuEntry == '1' and vowelCount == 5:
                print("No more vowels available!")
            elif menuEntry == '1':
                tempWinnings[playerTurn - 1] -= 250
                endTurn = guessVowel()
                displayWord()
            elif menuEntry == '2':
                guessWord()
                endTurn = 1
            else:
                endTurn = 1

    endTurn = 0
    print(f"{playerTurn} turn complete, tempwinnings are {tempWinnings}")       #DEBUGGING
    
print("2 rounds complete!")
'''
for i in range(1,4)             
    add tempWinnings[i] to winnings[i]          #bank winnings
tempWinnings = [0,0,0]
vowelCount = 0
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