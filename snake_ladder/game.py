from dice import Dice
from player import Player
from jumper import Jumper
from game_board import GameBoard


def main():
    print("🎲 Welcome to Snake and Ladder!")
    p1_name = input("Enter Player 1 name: ")
    p2_name = input("Enter Player 2 name: ")

    players = [Player(p1_name, id=1), Player(p2_name, id=2)]
    dice = Dice()

    # Add your own snakes and ladders here
    snakes = [Jumper(99, 21), Jumper(70, 55), Jumper(52, 42)]
    ladders = [Jumper(3, 22), Jumper(5, 8), Jumper(11, 26), Jumper(20, 29)]
    board = GameBoard(snakes, ladders)

    current = 0
    while True:
        player = players[current]
        input(f"\n{player.name}'s turn 🎲 (press Enter to roll the dice)")
        roll = dice.roll()
        print(f"{player.name} rolled a {roll} 🎯")

        if player.position + roll > board.board_size:
            print(f"❌ Can't move, need exact number to reach 100.")
        else:
            player.position += roll
            player.position = board.apply_jumpers(player.position)
            print(f"{player.name} is now at position {player.position}")

            if player.position == board.board_size:
                print(f"🎉 {player.name} wins the game!")
                break

        current = (current + 1) % len(players)


if __name__ == "__main__":
    main()
