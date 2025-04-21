class Jumper:
    def __init__(self, start_position: int, end_position: int):
        self.end_position = end_position
        self.start_position = start_position
        
        
    # def __init__(self, board):
    #     self.board = board
    #     self.position = 0
    #     self.jumps = 0

    # def jump(self, steps):
    #     if self.position + steps < len(self.board):
    #         self.position += steps
    #         self.jumps += 1
    #         return True
    #     else:
    #         return False

    # def get_position(self):
    #     return self.position

    # def get_jumps(self):
        # return self.jumps
