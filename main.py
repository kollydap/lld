from snake_ladder.dice import Dice
from snake_ladder.game_board import GameBoard
from snake_ladder.player import Player
from snake_ladder.jumper import Jumper

# Main game loop
# Game initialization

if __name__ == "__main__":
    dice = Dice()

    players = [Player("Alice", 1), Player("Bob", 2)]

    # Define a few snakes and ladders
    snakes = [Jumper(99, 21), Jumper(70, 55), Jumper(52, 42)]  # valid snake

    ladders = [Jumper(5, 25), Jumper(40, 85), Jumper(28, 89)]  # valid ladder

    game = GameBoard(dice, players, snakes, ladders)
    game.start_game()
