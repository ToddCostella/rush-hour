from enum import Enum
from dataclasses import dataclass
from typing import NewType, Tuple, List
import copy
from rich.console import Console
from getch import getch
from rich.table import Table
from rich.live import Live


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Color(Enum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"
    PURPLE = "purple"
    BROWN = "brown"
    WHITE = "white"
    ORANGE = "dark_orange"
    YELLOW = "yellow"
    CYAN = "cyan"


class Orientation(Enum):
    HORIZONTAL = "H"
    VERTICAL = "V"


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
    puzzle_entries: List[PuzzleEntry]


@dataclass
class VehiclePlacement:
    car: Car
    orientation: Orientation
    coverage: list[int]


@dataclass
class Move:
    car: Car
    direction: Direction


class Game:
    SIZE: int = 6
    EXIT_SQUARE: int = 18

    def __init__(self, puzzle_card: PuzzleCard) -> None:
        vehicle_placements = []
        for puzzle_entry in puzzle_card.puzzle_entries:
            placment = VehiclePlacement(
                car=puzzle_entry.car,
                orientation=puzzle_entry.orientation,
                coverage=self.calculate_coverage_squares_from_puzzle_entry(
                    puzzle_entry=puzzle_entry
                ),
            )
            vehicle_placements.append(placment)
        # TODO: Check that we have one RED vehicle and that we don't have any vehicle ids that would collide with the hjkl navigation keys

        self.vehicle_placements: list[VehiclePlacement] = vehicle_placements
        self.moves = []
        self.is_puzzle_solved = False
        self.console = Console()

    def calculate_vehicle_placement_coverage(
        self, exclude_car: Car | None = None
    ) -> list[int]:
        return sorted(
            square
            for placement in self.vehicle_placements
            if exclude_car is None or placement.car.id != exclude_car.id
            for square in self.calculate_coverage_squares(
                placement.coverage[0],
                car=placement.car,
                orientation=placement.orientation,
            )
        )

    def calculate_vehicle_placement_coverage_for_all(self) -> list[int]:
        return self.calculate_vehicle_placement_coverage()

    def calculate_vehicle_placement_coverage_for_others(self, car: Car) -> list[int]:
        return self.calculate_vehicle_placement_coverage(exclude_car=car)

    def get_vehicle_placement_for_car(self, car: Car) -> VehiclePlacement:
        match = [
            placement
            for placement in self.vehicle_placements
            if placement.car.id == car.id
        ]
        return match[0]

    def move(self, move: Move) -> Tuple[bool, VehiclePlacement]:
        placement = self.get_vehicle_placement_for_car(move.car)
        new_placement = copy.copy(placement)
        (is_valid_move, new_pos) = self.is_valid_move(move)
        if is_valid_move:
            my_new_squares = self.calculate_coverage_squares(
                start_square=new_pos,
                car=new_placement.car,
                orientation=new_placement.orientation,
            )
            new_placement.coverage = my_new_squares

            self.moves.append(move)
            # Update the list of vehicle_placements by removing the old placement and replacing it with the new placement
            self.vehicle_placements.remove(placement)
            self.vehicle_placements.append(new_placement)
        return is_valid_move, new_placement

    def is_valid_move(self, move: Move) -> Tuple[bool, int]:
        is_valid = False
        new_pos = 0

        other_vehicle_sqaures = self.calculate_vehicle_placement_coverage_for_others(
            move.car
        )

        placement = self.get_vehicle_placement_for_car(move.car)
        head_pos = min(placement.coverage)
        tail_pos = max(placement.coverage)
        match move.direction:
            case Direction.UP:
                new_pos = head_pos - self.SIZE
                is_valid = new_pos > 0 and placement.orientation == Orientation.VERTICAL
            case Direction.DOWN:
                new_pos = head_pos + self.SIZE
                is_valid = (
                    tail_pos + self.SIZE <= (self.SIZE * self.SIZE)
                    and placement.orientation == Orientation.VERTICAL
                )
            case Direction.LEFT:
                new_pos = head_pos - 1
                has_not_underflowed_row = new_pos > 0
                has_not_underflowed_column = head_pos % self.SIZE != 1
                is_valid = (
                    has_not_underflowed_column
                    and has_not_underflowed_row
                    and placement.orientation == Orientation.HORIZONTAL
                )
            case Direction.RIGHT:
                new_pos = head_pos + 1
                has_not_overflowed_row = new_pos < (self.SIZE * self.SIZE)
                has_not_overflowed_column = tail_pos % self.SIZE != 0
                is_valid = (
                    has_not_overflowed_column
                    and has_not_overflowed_row
                    and placement.orientation == Orientation.HORIZONTAL
                )
        new_coverage = self.calculate_coverage_squares(
            new_pos,
            move.car,
            placement.orientation,
        )
        is_valid = is_valid and not any(
            item in other_vehicle_sqaures for item in new_coverage
        )
        # The one exception to all these rules is that Car X (The players RED car) can exit the board from position 18 to solve the puzzle
        if (
            move.car.id == VehicleID("X")
            and move.direction == Direction.RIGHT
            and tail_pos == 18
        ):
            self.is_puzzle_solved = True
            is_valid = True
            new_pos = 99  # Not really valid but we need to some value to indicate off the board

        return is_valid, new_pos

    def calculate_coverage_squares_from_puzzle_entry(
        self, puzzle_entry: PuzzleEntry
    ) -> list[int]:

        return self.calculate_coverage_squares(
            start_square=puzzle_entry.starting_position,
            car=puzzle_entry.car,
            orientation=puzzle_entry.orientation,
        )

    def calculate_coverage_squares(
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

    def positions_as_rich_table(self, selected_car) -> Table:
        car_squares = {
            square: p.car for p in self.vehicle_placements for square in p.coverage
        }
        table = Table(show_header=False, show_lines=False)
        for _ in range(1, self.SIZE):
            table.add_column()

        grid = Table.grid(expand=True)
        grid.add_column()

        for row in range(0, self.SIZE):
            row_text: list[str] = []
            for column in range(1, self.SIZE + 1):
                square = row * self.SIZE + column
                contents = ""
                if square in car_squares:
                    car = car_squares[square]
                    contents = f"[black on {car.color.value}] {car.id} [/]"
                else:
                    contents = "   "
                    # contents = f"[white]{square:2} [/]"

                # Add a visual indicator where the exit square is on the board
                if square == self.EXIT_SQUARE:
                    contents = contents + "[yellow]|[/]"

                row_text.append(contents)

            table.add_row(*row_text)
        grid.add_row(table)
        status_row = (
            "Car:None"
            if selected_car is None
            else f"[black on {selected_car.color.value}] Car:{selected_car.id}[/]"
        )

        # TODO: Add a colspan here and set the moves lavel to be right justified
        status_row = status_row + f"  Moves:{len(self.moves)}"
        grid.add_row(status_row)
        return grid


def build_puzzle_card_from_definition(definition: str) -> PuzzleCard:
    tokens = definition.split(",")
    color_dict = {
        "R": Color.RED,
        "O": Color.ORANGE,
        "B": Color.BLUE,
        "P": Color.PURPLE,
        "G": Color.GREEN,
        "Y": Color.YELLOW,
        "C": Color.CYAN,
    }
    puzzle_entries: list[PuzzleEntry] = []
    for token in tokens:
        car_id_token = token[0]
        color_token = token[1]
        lenth_token = token[2]
        orientation_token = token[3]
        starting_position_token = token[4] + token[5]

        assert len(car_id_token) == 1
        assert color_token in color_dict.keys()
        assert lenth_token in ["2", "3"]
        assert orientation_token in ["H", "V"]
        car_id = VehicleID(car_id_token)
        car_color = color_dict[color_token]
        car_length = int(lenth_token)

        car_orientation = {o.value: o for o in Orientation}[orientation_token]
        starting_position = int(starting_position_token)
        assert starting_position > 0 and starting_position < 37
        car = Car(id=car_id, color=car_color, length=car_length)
        puzzle_entry = PuzzleEntry(
            car=car, orientation=car_orientation, starting_position=starting_position
        )

        puzzle_entries.append(puzzle_entry)

    return PuzzleCard(puzzle_entries)


if __name__ == "__main__":
    # TODO: These puzzles need to be pulled out into a puzzle deck or puzzle library
    puzzle_one = "XR2H14,AG2H01,BO2V25,CC2H29,PP3V07,TB3V10,OY3V06,RG3H33"
    puzzle_two = (
        "XR2H13,AG2V01,BY3H04,CC2V10,DP3V12,EB2V17,FO2H29,GG2H31,MC2V27,NB2H34,OB3H19"
    )
    puzzle_three = "XR2H14,AG2H20,BY3V16,CC3V24,EB2H33,FO2V26"
    puzzle_four = "XR2H14,AY3V01,BP3V04,CG2V21,EB3H22,FO2V30,GY3H33"
    puzzle_card = build_puzzle_card_from_definition(puzzle_one)
    g = Game(puzzle_card)
    car = None
    move_dict = {
        "h": Direction.LEFT,
        "j": Direction.DOWN,
        "k": Direction.UP,
        "l": Direction.RIGHT,
    }
    car_dict = {p.car.id.lower(): p.car for p in g.vehicle_placements}
    with Live(
        g.positions_as_rich_table(selected_car=car), screen=False, auto_refresh=False
    ) as live:
        direction = Direction.DOWN
        car = None

        while True:
            key = getch()
            move = False
            if key in car_dict.keys():
                car = car_dict[key]
            if key in move_dict.keys():
                move = True
                direction = move_dict[key]
            if key == "q":
                break
            if move and car:
                is_valid_move, _ = g.move(Move(car=car, direction=direction))
                if g.is_puzzle_solved:
                    break

                live.update(g.positions_as_rich_table(selected_car=car), refresh=True)
                if not is_valid_move:
                    g.console.bell()
    game_moves = [{m.car.id: m.direction.name} for m in g.moves]
    g.console.print(game_moves)
