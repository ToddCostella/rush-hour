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
    id: VehicleID
    color: Color
    length: int


@dataclass
class VehiclePlacement:
    car: Car
    orientation: Orientation
    start_square: int


class Game:
    SIZE: int = 6

    def __init__(self, vehicle_placements) -> None:
        self.vehicle_placements = vehicle_placements

    def calculate_vehicle_placement_coverage_for_all(self) -> list[int]:
        coverage = []
        for p in self.vehicle_placements:
            coverage.append(
                self.calculate_vehicle_placement_squares(vehicle_placement=p)
            )
        flattened_list = [item for sublist in coverage for item in sublist]
        return flattened_list

    def calculate_vehicle_placement_coverage_for_others(
        self, id: VehicleID
    ) -> list[int]:
        coverage = []
        for p in self.vehicle_placements:
            if p.car.id != id:
                coverage.append(
                    self.calculate_vehicle_placement_squares(vehicle_placement=p)
                )
        flattened_list = sorted([item for sublist in coverage for item in sublist])
        return flattened_list

    def get_vehicle_placement_by_identifier(
        self, id: VehicleID
    ) -> VehiclePlacement | None:
        match = [
            placement for placement in self.vehicle_placements if placement.car.id == id
        ]
        return match[0] if len(match) == 1 else None

    def get_my_squares_from_board(self, id: VehicleID) -> list[int]:
        placement = self.get_vehicle_placement_by_identifier(id)
        my_squares = []
        if placement is not None:
            my_squares = self.calculate_vehicle_placement_squares(placement)

        return my_squares

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
        is_valid = False
        match direction:
            case Direction.UP:
                new_pos = current_pos - self.SIZE
                is_valid = new_pos > 0
            case Direction.DOWN:
                new_pos = current_pos + self.SIZE
                is_valid = new_pos < (self.SIZE * self.SIZE)
            case Direction.LEFT:
                new_pos = current_pos - 1
                has_not_underflowed_row = new_pos > 0
                has_not_underflowed_column = current_pos % self.SIZE != 1
                is_valid = has_not_underflowed_column and has_not_underflowed_row
            case Direction.RIGHT:
                new_pos = current_pos + 1
                has_not_overflowed_row = new_pos < (self.SIZE * self.SIZE)
                has_not_overflowed_column = current_pos % self.SIZE != 0
                is_valid = has_not_overflowed_column and has_not_overflowed_row
        return is_valid

    def calculate_vehicle_placement_squares(
        self, vehicle_placement: VehiclePlacement
    ) -> list[int]:
        squares = []
        if vehicle_placement.orientation == Orientation.HORIZONTAL:
            squares = list(
                range(
                    vehicle_placement.start_square,
                    vehicle_placement.start_square + vehicle_placement.car.length,
                )
            )
        if vehicle_placement.orientation == Orientation.VERTICAL:
            for vertical_placement in range(0, vehicle_placement.car.length):
                squares.append(
                    vehicle_placement.start_square + (vertical_placement * self.SIZE)
                )
        return squares

    moves: list[int]


# if __name__ == "__main__":
#    g = Game()
