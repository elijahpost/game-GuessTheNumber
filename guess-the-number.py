import random
import sys
if sys.version_info.major != 3:
    print ('\n >>> This program requires Python 3.x.x to run. <<<\n')
    sys.exit()

class self:
    name = None
    score = 0
    lastLevelCleared = 0

    @classmethod     # I have two housemates who heped me with this this def. It works but I don't know how...yet. (4/20/20)
    def resetSelf(self):
        self.name = None
        self.score = 0
        self.lastLevelCleared = 0
        # down the road, I suppose that we could spin up instances of players, and potentially have an all-time score that we could save, or something to that end.

    def welcome():
        print ('\nEnter your name:')
        self.name = input()
        print ('\nHello, ' + self.name + '. \n')

    def gameOver():
        print ('\nGame Over, ' + self.name + '.')
        print ('Final Score: ' + str(self.score))
        restartPrompt()
    
    def levelClear(levelNum, levelScore):
        self.lastLevelCleared = self.lastLevelCleared + 1
        print ('\n### ' + self.name + ' HAS CLEARED LEVEL ' + str(levelNum) + ' ###\n')
        print ('Level Score: ' + str(levelScore) + '\n' + 'Total Score: ' + str(self.score) + '\n')

    def gameClear():
        print('\n' + '###########################' + '\n' + '## HOLY SMOKES, YOU WON! ##' + '\n' + '###########################' + '\n')
        print(self.name + '\'s FINAL SCORE: ' + str(self.score))
        restartPrompt()

    def level(levelNum, minNum, maxNum, maxGuesses):
        def outOfGuesses ():
            print('The correct number was ' + str(secretNum) + '.')
            self.gameOver()
        secretNum = random.randint(minNum, maxNum)
        remainingGuesses = maxGuesses - 1
        print ('############ LEVEL ' + str(levelNum) + ' ############# \n')
        print ('I am thinking of a number between ' + str(minNum) + ' and ' + str(maxNum) + '. You get ' + str((maxGuesses)) + ' guesses.') # could I print the randint arguements from directly above?
        for guessCounter in range(1,maxGuesses+1):
            print('\nGo for it, take a guess:')
            playerGuess = input()
            remainingGuesses = maxGuesses - guessCounter
            try:
                if int(playerGuess) == secretNum:
                    levelScore = maxGuesses - guessCounter
                    self.score = self.score + levelScore
                    print ('\nThat\'s It! You guessed it! \n')
                    break
                elif int(playerGuess) < secretNum:
                    print('Nope, ' + str(playerGuess) + ' is too low. You have ' + str(remainingGuesses) + ' guesses left.')
                elif int(playerGuess) > secretNum:
                    print('Nope, ' + str(playerGuess) + ' is too high. You have ' + str(remainingGuesses) + ' guesses left.')
            except (ValueError):
                print('"' + str(playerGuess) + '" is not a number. You have ' + str(remainingGuesses) + ' guesses left.')
        if int(playerGuess) == secretNum:
            self.levelClear(levelNum, levelScore)
        if playerGuess != str(secretNum):
            outOfGuesses()
        elif int(playerGuess) != secretNum:
            outOfGuesses()

def restartPrompt():
    playAgain = None
    while playAgain != 'y' or 'n':
        print ('\nThink you can do better? (y/n)')
        playAgain = input()
        if playAgain == 'y':
            self.resetSelf()
            main()
        elif playAgain == 'n':
            sys.exit()

def main():
    self.welcome()
    self.level(1, 1, 10, 7)
    self.level(2, 1, 20, 7)
    self.level(3, -5, 5, 5)
    self.level(4, 14, 17, 2)
    self.level(5, 20, 80, 10)
    self.level('BANANA', -1000, 2500, 20)
    self.gameClear()

main()