import random
class Dice:
    def __init__(self, number_of_dice: int = 1):
        self.number_of_dice = number_of_dice

    def roll(self):
        return random.randint(1 * self.number_of_dice, 6 * self.number_of_dice)
