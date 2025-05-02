from bottle_color.colors import Colors
class Bottle:
    def __init__(self, capacity: int, content :list = [None]):
        self.capacity = capacity
        self.content = content

    def __str__(self):
        return f"Bottle(color={self.capacity})"
    
    

    def __repr__(self):
        return self.__str__()
    
    def fillup(self, color: Colors):
        if len(self.content) >= self.capacity:
            print("Bottle is full")
            return
        if self.content[0]. != color:
            print("Cannot fill with different color")
            return
        self.content.append(color)
        