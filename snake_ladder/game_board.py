from .dice import Dice
from .jumper import Jumper
from .player import Player


class GameBoard:
    def __init__(
        self,
        dice: Dice,
        players_current_position: dict,
        snakes: list,
        ladders: list,
        next_turn,
        board_size: int,
    ):

        self.dice = dice
        self.board = self.create_board()
        self.players_current_position = players_current_position
        self.board_size = board_size
        self.ladders = ladders
        self.snakes = snakes
        self.next_turn = next_turn

    def start_game(self):
        # while True:
        while len(self.nextTurn) > 1:
            player = self.next_turn.pop(0)
            print(f"Player {player}'s turn")
            # * we get current position of player
            current_position = self.players_current_position[player.name]
            # * we roll the dice
            dice_value = self.dice.roll()
            # we get the next cell or position
            next_cell = current_position + dice_value
            # check if the next cell is greater than the board size
            if next_cell > self.board_size:
                self.next_turn.append(player)
                print(f"Player {player} rolled a {dice_value} and cannot move.")
                continue
            elif next_cell == self.board_size:
                print(f"Player {player} rolled a {dice_value} and wins!")
                self.players_current_position[player.name] = next_cell
                break
            else:
                print(f"Player {player} rolled a {dice_value} and moved to {next_cell}")
                self.players_current_position[player.name] = next_cell

    def create_board(self):
        board = {}
        for i in range(1, self.size + 1):
            board[i] = None
        return board

    def add_snake(self, start, end):
        if start in self.board and end in self.board:
            self.board[start] = end

    def add_ladder(self, start, end):
        if start in self.board and end in self.board:
            self.board[start] = end

    def get_destination(self, position):
        return self.board.get(position, position)
