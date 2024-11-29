from dataclasses import dataclass

@dataclass
class Movement:
    dx: int
    dy: int


class Location:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):
            return NotImplemented
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"Location({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def move(self, direction: Movement) -> bool:
        self.x += direction.dx
        self.y += direction.dy
        return True


class Robot:
    def __init__(self, location: Location) -> None:
        self.location = location

    def move(self, direction: Movement) -> bool:
        result = self.location.move(direction)
        return result


