from enum import Enum
from icecream import ic
from dataclasses import dataclass
from typing import NewType


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Color(Enum):
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


VehicleID = NewType("VehicleID", str)


@dataclass
class Car:
    identifier: VehicleID
    color: Color
    length: int


@dataclass
class VehiclePlacement:
    car: Car
    orientation: Orientation
    start_square: int


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

    # Returns a list of board placements given a car and it's initial placement
    def calculate_vehicle_placement_coverage(
        self, vehicle_placement: VehiclePlacement
    ) -> list[int]:
        placements = []
        if vehicle_placement.orientation == Orientation.HORIZONTAL:
            placements = list(
                range(
                    vehicle_placement.start_square,
                    vehicle_placement.start_square + vehicle_placement.car.length,
                )
            )
        if vehicle_placement.orientation == Orientation.VERTICAL:
            for vertical_placement in range(0, vehicle_placement.car.length):
                placements.append(
                    vehicle_placement.start_square + (vertical_placement * self.SIZE)
                )
        return placements


class Game:
    def __init__(self, vehicle_placements) -> None:
        self.board = Board()
        self.vehicle_placements = vehicle_placements

    def calculate_vehicle_placement_coverage_for_all(self) -> list[int]:
        coverage = []
        for p in self.vehicle_placements:
            coverage.append(
                self.board.calculate_vehicle_placement_coverage(vehicle_placement=p)
            )

        flattened_list = [item for sublist in coverage for item in sublist]
        return flattened_list

    moves: list[int]


# if __name__ == "__main__":
#    g = Game()
