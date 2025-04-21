class Dice:
    def __init__(self, number_of_dice: int = 1):
        self.value = 0
        self.number_of_dice = number_of_dice

    def roll(self):
        import random

        self.value = random.randint(1 * self.number_of_dice, 6 * self.number_of_dice)
        return self.value

    def get_value(self):
        return self.value
