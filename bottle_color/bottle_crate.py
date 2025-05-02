from bottle_color.bottles import Bottle
from bottle_color.colors import Colors


class BottleCrate:
    def __init__(self, bottles: list):
        self.bottles = bottles

    def __str__(self):
        return f"BottleCrate(bottles={self.bottles})"

    def create_bottle(self, capacity: int, number_of_bottles: int):
        for _ in range(number_of_bottles):
            content = [Colors("red")]
            bottle = Bottle(capacity, content=[])
            self.bottles.append(bottle)
            return bottle
