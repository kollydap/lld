import random
from typing import List


class Colors:
    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Colors) and self.name == other.name

    def __repr__(self):
        return self.name


class Bottle:
    def __init__(self, capacity: int, content: List[Colors] = None):
        self.capacity = capacity
        self.content = content or []

    def __str__(self):
        return f"Bottle({self.content})"

    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        return len(self.content) == 0

    def is_full(self):
        return len(self.content) == self.capacity

    def top_color(self):
        return self.content[-1] if self.content else None

    def available_space(self):
        return self.capacity - len(self.content)

    def can_pour_into(self, target_bottle):
        if self.is_empty():
            return False
        if target_bottle.is_full():
            return False
        if target_bottle.is_empty():
            return True
        return self.top_color() == target_bottle.top_color()

    def pour_into(self, target_bottle):
        if not self.can_pour_into(target_bottle):
            print("❌ Invalid move.")
            return False

        color_to_pour = self.top_color()
        count = 0

        # Count how many top elements have the same color
        for c in reversed(self.content):
            if c == color_to_pour:
                count += 1
            else:
                break

        # Calculate how many can actually be poured
        space = target_bottle.available_space()
        move_count = min(count, space)

        # Perform the move
        for _ in range(move_count):
            target_bottle.content.append(self.content.pop())

        print(f"✅ Poured {move_count} unit(s) of {color_to_pour.name} into target bottle.")
        return True


class BottleCrate:
    def __init__(self):
        self.bottles: List[Bottle] = []

    def __str__(self):
        return "\n".join([f"Bottle {i+1}: {bottle.content}" for i, bottle in enumerate(self.bottles)])

    def initialize_game(self, capacity: int, color_count: int, empty_bottles: int):
        total_bottles = color_count + empty_bottles
        COLORS_POOL = [Colors(name) for name in ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "pink"]]
        selected_colors = COLORS_POOL[:color_count]

        # Create shuffled pool of colors
        color_pool = []
        for color in selected_colors:
            color_pool.extend([color] * capacity)
        random.shuffle(color_pool)

        # Fill colored bottles
        for _ in range(color_count):
            content = [color_pool.pop() for _ in range(capacity)]
            self.bottles.append(Bottle(capacity, content))

        # Add empty bottles
        for _ in range(empty_bottles):
            self.bottles.append(Bottle(capacity, []))

    def is_game_won(self):
        for bottle in self.bottles:
            if bottle.is_empty():
                continue
            if not bottle.is_full():
                return False
            if any(c != bottle.top_color() for c in bottle.content):
                return False
        return True
