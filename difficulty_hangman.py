import random
HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
   |   |
       |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
   |   |
   |   |
       |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
   |   |
   |   |
  /    |
       |
 =========''', '''

   +---+
   |   |
   O   |
  /|\  |
   |   |
   |   |
  / \  |
       |
 =========''', '''

   +---+
   |   |
   O   |
 (/|\  |
   |   |
   |   |
  / \  |
       |
 =========''', '''

   +---+
   |   |
   O   |
 (/|\) |
   |   |
   |   |
  / \  |
       |
 =========''']

words = {'easy':'cat cow sun bug lips coat kite milk hat dog bird boy'.split(),
         'medium':'baseball mattress pinwheel lawnmower mailman bicycle password computer notebook cowboy circus desktop'.split(),
         'hard':'exponential parody philosopher opaque stockholder archaeologist twang addendum eureka observatory stowaway aristocrat'.split()}


def getRandomWord(wordDict):
	return random.choice(wordDict);
    # This function returns a random string from the passed dictionary of list of strings, and the key also.
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))
    #Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)
    return [wordDict[wordKey][wordIndex], wordKey]

def chooseEasy(yourChoice):
    wordKeyEasy = random.choice(yourChoice['easy'])
    wordKeyMedium = random.choice(yourChoice['medium'])
    wordKeyHard = random.choice(yourChoice['hard'])
    if yourChoice in words['easy']:
        print (wordKeyEasy)
        print('Good choice with easy!')
    elif yourChoice in words['medium']:
        return [wordKeyMedium]
    elif yourChoice in words['hard']:
        return wordKeyHard
    else:
        print('You broke my game!')
    
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()


def getGuess (alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print ('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
print('Select the difficulty level: ')
print('Easy Medium or Hard ')
difficultyChoice = input()
# assuming that difficultyChoice is on eof the proper terms.
print(words.difficultyChoice)
secretWord = getRandomWord(words.difficultyChoice)

print(secretWord)
exit


secretWord
selectDifficulty = chooseEasy(words), getRandomWord(words)

missedLetters = ''
correctLetters = ''
gameIsDone = False


while True:
    print('Good luck! Guess a letter.')
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    # Let the player type in a letter.
    guess = getGuess (missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
               foundAllLetters = False
               break
        if foundAllLetters:
               print('Yes! The secret word is " ' + secretWord + ' "! You have won!')
               gameIsDone = True
    else:
        missedLetters = missedLetters + guess

            # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard (HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, selectDifficulty = getRandomWord(words)
        else:
            break
            
