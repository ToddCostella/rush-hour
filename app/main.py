from enum import Enum
from icecream import ic
from dataclasses import dataclass
from typing import NewType, Tuple, List
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
class PuzzleEntry:
    car: Car
    orientation: Orientation
    starting_position: int


@dataclass
class PuzzleCard:
    setup: List[PuzzleEntry]


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

    def __init__(self, puzzle_card: PuzzleCard) -> None:
        vehicle_placements = []
        for puzzle_entry in puzzle_card.setup:
            placment = VehiclePlacement(
                puzzle_entry.car,
                puzzle_entry.orientation,
                self.calculate_vehicle_placement_squares(
                    puzzle_entry.starting_position,
                    puzzle_entry.car,
                    puzzle_entry.orientation,
                ),
            )
            vehicle_placements.append(placment)
        self.vehicle_placements: list[VehiclePlacement] = vehicle_placements
        self.moves = []

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

    def get_vehicle_placement_for_car(self, car: Car) -> VehiclePlacement:
        match = [
            placement
            for placement in self.vehicle_placements
            if placement.car.id == car.id
        ]
        return match[0]

    def get_my_squares_from_board(self, car: Car) -> list[int]:
        placement = self.get_vehicle_placement_for_car(car)
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

        # Update the list of vehicle_placements by removing the old placement and replacing it with the new placement
        self.vehicle_placements.remove(move.vehicle_placement)
        self.vehicle_placements.append(new_placement)
        self.moves.append(move)
        return is_valid_move, new_placement

    def is_valid_move(self, move: Move) -> Tuple[bool, int]:
        is_valid = False
        new_pos = 0

        other_vehicle_sqaures = self.calculate_vehicle_placement_coverage_for_others(
            move.vehicle_placement.car.id
        )

        current_pos = min(move.vehicle_placement.coverage)
        match move.direction:
            case Direction.UP:
                new_pos = current_pos - self.SIZE
                is_valid = (
                    new_pos > 0
                    and move.vehicle_placement.orientation == Orientation.VERTICAL
                )
            case Direction.DOWN:
                new_pos = current_pos + self.SIZE
                is_valid = (
                    new_pos < (self.SIZE * self.SIZE)
                    and move.vehicle_placement.orientation == Orientation.VERTICAL
                )
            case Direction.LEFT:
                new_pos = current_pos - 1
                has_not_underflowed_row = new_pos > 0
                has_not_underflowed_column = current_pos % self.SIZE != 1
                is_valid = (
                    has_not_underflowed_column
                    and has_not_underflowed_row
                    and move.vehicle_placement.orientation == Orientation.HORIZONTAL
                )
            case Direction.RIGHT:
                new_pos = current_pos + 1
                has_not_overflowed_row = new_pos < (self.SIZE * self.SIZE)
                has_not_overflowed_column = current_pos % self.SIZE != 0
                is_valid = (
                    has_not_overflowed_column
                    and has_not_overflowed_row
                    and move.vehicle_placement.orientation == Orientation.HORIZONTAL
                )
        new_coverage = self.calculate_vehicle_placement_squares(
            new_pos,
            move.vehicle_placement.car,
            move.vehicle_placement.orientation,
        )
        is_valid = is_valid and not any(
            item in other_vehicle_sqaures for item in new_coverage
        )
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

    def print_game(self):
        # Geneate a dictionary in which the keys are the the number of the square occupied and the vlaue is the car occupying the square
        car_squares = {
            square: p.car for p in self.vehicle_placements for square in p.coverage
        }
        print("")
        for row in range(0, self.SIZE):
            for column in range(1, self.SIZE + 1):
                square = row * self.SIZE + column
                # If the square is occupied, print the car id, otherwise print the number of the square
                if square in car_squares:
                    car = car_squares[square]
                    print(f"| {car.id} ", end="")
                else:
                    print(f"|{square:2} ", end="")
                if column % self.SIZE == 0:
                    print("|")


# if __name__ == "__main__":
#    g = Game()
