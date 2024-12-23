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
            raise Exception("Not Implemented")
        return positions


# TODO: Move this out to some sort of config file or something
class Game:
    initial_setup = [
        Position(
            car=Car(identifier="A", colour=Colour.GREEN, length=2),
            orientation=Orientation.HORIZONTAL,
            board_position=1,
        ),
        Position(
            Car(identifier="B", colour=Colour.PURPLE, length=3),
            orientation=Orientation.VERTICAL,
            board_position=7,
        ),
        Position(
            Car(identifier="C", colour=Colour.RED, length=2),
            orientation=Orientation.HORIZONTAL,
            board_position=14,
        ),
        Position(
            Car(identifier="D", colour=Colour.ORANGE, length=2),
            orientation=Orientation.VERTICAL,
            board_position=25,
        ),
        Position(
            Car(identifier="E", colour=Colour.GREEN, length=3),
            orientation=Orientation.HORIZONTAL,
            board_position=33,
        ),
        Position(
            Car(identifier="F", colour=Colour.BLUE, length=3),
            orientation=Orientation.VERTICAL,
            board_position=10,
        ),
        Position(
            Car(identifier="G", colour=Colour.BLUE, length=2),
            orientation=Orientation.HORIZONTAL,
            board_position=29,
        ),
        Position(
            Car(identifier="H", colour=Colour.YELLOW, length=3),
            orientation=Orientation.VERTICAL,
            board_position=6,
        ),
    ]
    moves: list[int]


if __name__ == "__main__":
    g = Game()
    ic(g.initial_setup)
