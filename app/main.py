from enum import Enum
from icecream import ic
from dataclasses import dataclass
from typing import NewType, Tuple
import copy


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
    coverage: list[int]


@dataclass
class Move:
    vehicle_placement: VehiclePlacement
    direction: Direction


class Game:
    SIZE: int = 6

    def __init__(self, vehicle_placements) -> None:
        # TODO populate coverage array for all placements. Using the first index of the array as the starting point. Seems smelly
        self.vehicle_placements = vehicle_placements

    def calculate_vehicle_placement_coverage_for_all(self) -> list[int]:
        coverage = []
        for p in self.vehicle_placements:
            coverage.append(
                self.calculate_vehicle_placement_squares(
                    p.coverage[0], car=p.car, orientation=p.orientation
                )
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
                    self.calculate_vehicle_placement_squares(
                        p.coverage[0], car=p.car, orientation=p.orientation
                    )
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
            my_squares = self.calculate_vehicle_placement_squares(
                start_square=placement.coverage[0],
                car=placement.car,
                orientation=placement.orientation,
            )

        return my_squares

    def move(self, move: Move) -> Tuple[bool, VehiclePlacement]:
        new_placement = copy.copy(move.vehicle_placement)
        (is_valid_move, new_pos) = self.is_valid_move(move)
        if is_valid_move:
            my_new_squares = self.calculate_vehicle_placement_squares(
                start_square=new_pos,
                car=new_placement.car,
                orientation=new_placement.orientation,
            )
            new_placement.coverage = my_new_squares

        return (is_valid_move, new_placement)

    # TODO: Need to add collistion logic here
    def is_valid_move(self, move: Move) -> Tuple[bool, int]:
        is_valid = False
        new_pos = 0

        match move.direction:
            case Direction.UP:
                current_pos = min(move.vehicle_placement.coverage)
                new_pos = current_pos - self.SIZE
                is_valid = new_pos > 0
            case Direction.DOWN:
                current_pos = max(move.vehicle_placement.coverage)
                new_pos = current_pos + self.SIZE
                is_valid = new_pos < (self.SIZE * self.SIZE)
            case Direction.LEFT:
                current_pos = min(move.vehicle_placement.coverage)
                new_pos = current_pos - 1
                has_not_underflowed_row = new_pos > 0
                has_not_underflowed_column = current_pos % self.SIZE != 1
                is_valid = has_not_underflowed_column and has_not_underflowed_row
            case Direction.RIGHT:
                current_pos = max(move.vehicle_placement.coverage)
                new_pos = current_pos + 1
                has_not_overflowed_row = new_pos < (self.SIZE * self.SIZE)
                has_not_overflowed_column = current_pos % self.SIZE != 0
                is_valid = has_not_overflowed_column and has_not_overflowed_row
        return (is_valid, new_pos)

    def calculate_vehicle_placement_squares(
        self, start_square: int, car: Car, orientation: Orientation
    ) -> list[int]:
        squares = []

        if orientation == Orientation.HORIZONTAL:
            squares = list(
                range(
                    start_square,
                    start_square + car.length,
                )
            )
        if orientation == Orientation.VERTICAL:
            for placement in range(0, car.length):
                squares.append(start_square + (placement * self.SIZE))
        return squares

    moves: list[int]


# if __name__ == "__main__":
#    g = Game()
