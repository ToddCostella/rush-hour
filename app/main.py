from enum import Enum
from icecream import ic


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Board:
    SIZE: int = 6

    def move_up(self, current_pos: int) -> int:
        return (
            current_pos - self.SIZE
            if self.is_valid_move(current_pos, Direction.UP)
            else 0
        )

    def move_down(self, current_pos: int) -> int:
        return (
            current_pos + self.SIZE
            if self.is_valid_move(current_pos, Direction.DOWN)
            else 0
        )

    def move_left(self, current_pos: int) -> int:
        return current_pos - 1 if self.is_valid_move(current_pos, Direction.LEFT) else 0

    def move_right(self, current_pos: int) -> int:
        return (
            current_pos + 1 if self.is_valid_move(current_pos, Direction.RIGHT) else 0
        )

    def is_valid_move(self, current_pos: int, direction: Direction) -> bool:
        match direction:
            case Direction.UP:
                new_pos = current_pos - self.SIZE
                return new_pos > 0
            case Direction.DOWN:
                new_pos = current_pos + self.SIZE
                return new_pos < (self.SIZE * self.SIZE)
            case Direction.LEFT:
                new_pos = current_pos - 1
                has_not_underflowed_row = new_pos > 0
                has_not_underflowed_column = current_pos % self.SIZE != 1
                return has_not_underflowed_column and has_not_underflowed_row
            case Direction.RIGHT:
                new_pos = current_pos + 1
                has_not_overflowed_row = new_pos < (self.SIZE * self.SIZE)
                has_not_overflowed_column = current_pos % self.SIZE != 0
                return has_not_overflowed_column and has_not_overflowed_row


class Game:
    moves: list[int]
