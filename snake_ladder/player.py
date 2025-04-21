class Player:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.position = 0
        self.is_winner = False

    def move(self, steps: int):
        self.position += steps
        if self.position >= 100:
            self.position = 100
            self.is_winner = True
