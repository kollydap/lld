# # GameBoard
# class GameBoard:
#     def __init__(self, dice, players, snakes, ladders, board_size=100):
#         self.dice = dice
#         self.players = players
#         self.snakes = snakes
#         self.ladders = ladders
#         self.board_size = board_size
#         self.next_turn = players[:]  # Copy of list
#         self.players_current_position = {p.name: 0 for p in players}

#     def start_game(self):
#         while len(self.next_turn) > 1:
#             player = self.next_turn.pop(0)
#             print(f"\n🎲 {player.name}'s turn:")

#             current_position = self.players_current_position[player.name]
#             dice_value = self.dice.roll()
#             next_cell = current_position + dice_value

#             if next_cell > self.board_size:
#                 print(f"{player.name} rolled a {dice_value} and cannot move.")
#                 self.next_turn.append(player)
#                 continue

#             # Check snakes
#             for jumper in self.snakes:
#                 if next_cell == jumper.start_position and jumper.is_snake():
#                     print(f"🐍 {player.name} got bitten by a snake from {jumper.start_position} to {jumper.end_position}")
#                     next_cell = jumper.end_position

#             # Check ladders
#             for jumper in self.ladders:
#                 if next_cell == jumper.start_position:
#                     print(f"🪜 {player.name} climbed a ladder from {jumper.start_position} to {jumper.end_position}")
#                     next_cell = jumper.end_position

#             self.players_current_position[player.name] = next_cell
#             print(f"{player.name} moved to {next_cell}")

#             if next_cell == self.board_size:
#                 print(f"🎉 {player.name} wins the game!")
#                 break

#             self.next_turn.append(player)

from jumper import Jumper


class GameBoard:
    def __init__(self, snakes, ladders, board_size=100):
        self.snakes = snakes
        self.ladders = ladders
        self.board_size = board_size

    def apply_jumpers(self, position):
        while True:
            jumped = False
            for jumper in self.snakes + self.ladders:
                if position == jumper.start_position:
                    jump_type = "🐍 Snake" if jumper.is_snake() else "🪜 Ladder"
                    print(
                        f"{jump_type}! You moved from {jumper.start_position} to {jumper.end_position}"
                    )
                    position = jumper.end_position
                    jumped = True
                    break
            if not jumped:
                break
        return position
