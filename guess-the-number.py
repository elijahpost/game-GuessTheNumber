import random
import sys
if sys.version_info.major != 3:
    print ('\n >>> This program requires Python 3.x.x to run. <<<\n')
    sys.exit()

class game:
    name = None
    score = 0
    lastLevelCleared = 0

    @classmethod     # I have two housemates who heped me with this this def. It works but I don't know how...yet. (4/20/20)
    def reset(self):
        game.name = None
        game.score = 0
        game.lastLevelCleared = 0
        # down the road, I suppose that we could spin up instances of players, and potentially have an all-time score that we could save, or something to that end.

    def welcome():
        print ('\nEnter your name:')
        game.name = input()
        print ('\nHello, ' + game.name + '. \n')

    def gameOver():
        print ('\nGame Over, ' + game.name + '.')
        print ('Final Score: ' + str(game.score))
        restartPrompt()
    
    def levelClear(levelNum, levelScore):
        game.lastLevelCleared = game.lastLevelCleared + 1
        print ('\n### ' + game.name + ' HAS CLEARED LEVEL ' + str(levelNum) + ' ###\n')
        print ('Level Score: ' + str(levelScore) + '\n' + 'Total Score: ' + str(game.score) + '\n')

    def gameClear():
        print('\n' + '###########################' + '\n' + '## HOLY SMOKES, YOU WON! ##' + '\n' + '###########################' + '\n')
        print(game.name + '\'s FINAL SCORE: ' + str(game.score))
        restartPrompt()

    def level(levelNum, minNum, maxNum, maxGuesses):
        def outOfGuesses ():
            print('The correct number was ' + str(secretNum) + '.')
            game.gameOver()
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
                    game.score = game.score + levelScore
                    print ('\nThat\'s It! You guessed it! \n')
                    break
                elif int(playerGuess) < secretNum:
                    print('Nope, ' + str(playerGuess) + ' is too low. You have ' + str(remainingGuesses) + ' guesses left.')
                elif int(playerGuess) > secretNum:
                    print('Nope, ' + str(playerGuess) + ' is too high. You have ' + str(remainingGuesses) + ' guesses left.')
            except (ValueError):
                print('"' + str(playerGuess) + '" is not a number. You have ' + str(remainingGuesses) + ' guesses left.')
        if int(playerGuess) == secretNum:
            game.levelClear(levelNum, levelScore)
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
            game.reset()
            main()
        elif playAgain == 'n':
            sys.exit()

def main():
    game.welcome()
    game.level(1, 1, 10, 7)
    game.level(2, 1, 20, 7)
    game.level(3, -5, 5, 5)
    game.level(4, 14, 17, 2)
    game.level(5, 20, 80, 10)
    game.level('BANANA', -1000, 2500, 20)
    game.gameClear()

main()