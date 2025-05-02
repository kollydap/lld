class Jumper:
    def __init__(self, start_position: int, end_position: int):
        if start_position == end_position:
            raise ValueError("Start and end positions can't be the same")
        self.start_position = start_position
        self.end_position = end_position

    def is_snake(self):
        return self.start_position > self.end_position

    def is_ladder(self):
        return self.start_position < self.end_position
