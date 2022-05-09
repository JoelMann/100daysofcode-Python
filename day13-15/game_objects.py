import random

#this is useless, but i misread and thought I was making a DND game, so it stays
class Dice:
    def __init__(self, number_of_sides: int):
        self.number_of_sides = number_of_sides
    
    def roll(self):
        return random.randint(1,self.number_of_sides)

class Roll: 
    def __init__(self, name: str, defeats: str):
        self.name = name
        self.defeats = defeats

def didPlayerWin(playerRoll: Roll, comparisonRoll: Roll) -> int:
    if playerRoll.defeats == comparisonRoll.name:
        print("Player wins this round!")
        return 1
    elif comparisonRoll.defeats == playerRoll.name:
        print("Computer wins this round!")
        return -1
    else:
        print("Tie game!")
        return 0