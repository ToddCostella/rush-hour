from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Board:
    SIZE: int = 6

    def move_up(self, current_pos: int) -> int:
        return current_pos - self.SIZE

    def move_down(self, current_pos: int) -> int:
        return current_pos + self.SIZE

    def move_left(self, current_pos: int) -> int:
        return current_pos - 1

    def move_right(self, current_pos: int) -> int:
        return current_pos + 1

    def is_valid_move(self, current_pos: int, direction: int) -> bool:
        match direction:
            case Direction.UP:
                new_pos = self.move_up(current_pos)
                return new_pos > 0
            case Direction.DOWN:
                new_pos = self.move_down(current_pos)
                return new_pos < (self.SIZE * self.SIZE)
            case Direction.LEFT:
                new_pos = self.move_left(current_pos)
                return new_pos < 0 or new_pos % self.SIZE == 0
            case Direction.RIGHT:
                new_pos = self.move_right(current_pos)
                return new_pos < (self.SIZE * self.SIZE) or new_pos % self.SIZE == 0
            case _:
                return False


class Game:
    moves: list[int]
