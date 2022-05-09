import random

class Dice:
    def __init__(self, number_of_sides: int):
        self.number_of_sides = number_of_sides
    
    def roll(self):
        return random.randint(1,self.number_of_sides)