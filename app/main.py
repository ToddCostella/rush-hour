from enum import Enum
from icecream import ic
from dataclasses import dataclass


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Colour(Enum):
    BLUE = 1
    GREEN = 2
    RED = 3
    PURPLE = 4
    BROWN = 5
    WHITE = 6
    ORANGE = 7
    YELLOW = 8


class Orientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


@dataclass
class Car:
    identifier: str
    colour: Colour
    length: int
    orientation: Orientation 
    positions:list[int]


@dataclass
class Position:
    car: Car
    orientation: Orientation
    board_position: int


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

    # Returns a list of board positions given a car and it's initial position
    def calculate_position_coverage(self, position: Position) -> list[int]:
        positions = []
        if position.orientation == Orientation.HORIZONTAL:
            positions = list(
                range(
                    position.board_position,
                    position.board_position + position.car.length,
                )
            )
        if position.orientation == Orientation.VERTICAL:
            for vertical_position in range(0, position.car.length):
                positions.append(
                    position.board_position + (vertical_position * self.SIZE)
                )
        return positions


class Game:
    def __init__(self, positions) -> None:
        self.board = Board()
        self.positions = positions

    def get_car_by_id(self, id: str) -> Car | None:
        matches = [
            position for position in self.positions if position.car.identifier == id
        ]
        return matches[0].car if len(matches) > 0 and matches[0] is not None else None

    moves: list[int]


# if __name__ == "__main__":
#    g = Game()
