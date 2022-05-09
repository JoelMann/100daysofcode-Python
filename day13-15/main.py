from game_objects import *


def printHeader():
    print("WELCOME TO ROCK PAPER SCISSORS")
    print("ya, thats the assignment. Good luck")


def getAndValidateInput(dic: dict) -> str:
    getRoll = input("Roll a 'rock', 'paper', or 'scissors': ").lower()
    while getRoll not in dic:
        getRoll = input("Roll a 'rock', 'paper', or 'scissors': ").lower()
    return getRoll


def gameLoop(wins_to_end: int):
    rolls = {}
    rolls['rock'] = Roll('rock', 'scissors')
    rolls['paper'] = Roll('paper', 'rock')
    rolls['scissors'] = Roll('scissors', 'paper')
    computerOptions = list(rolls.keys())

    dice = Dice(3)
    PlayerWins = 0
    CompWins = 0
    while max(PlayerWins,CompWins) < wins_to_end:
        roll = getAndValidateInput(rolls)

        computerRoll = computerOptions[dice.roll()-1]
        print(f'Computer is playing {computerRoll}')

        round = didPlayerWin(rolls[roll], rolls[computerRoll])

        if round > 0:
            PlayerWins += 1
        elif round < 0:
            CompWins += 1
        else:
            continue
    print(f'Game is over. Score: Player got {PlayerWins} while computer got {CompWins}')


def main():
    printHeader()
    player = input("Please announce yourself: ")
    print(f'Welcome to this super exciting game, {player}')
    gameLoop(3)


if __name__ == "__main__":
    main()
