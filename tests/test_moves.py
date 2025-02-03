# from icecream import ic
from app.main import (
    Direction,
    Car,
    Color,
    Orientation,
    Game,
    VehicleID,
    Move,
    PuzzleEntry,
    PuzzleCard,
    build_puzzle_card_from_definition,
)
from rich.console import Console


console = Console()
car_x = Car(id=VehicleID("X"), color=Color.RED, length=2)
car_a = Car(id=VehicleID("A"), color=Color.BLUE, length=3)
car_b = Car(id=VehicleID("B"), color=Color.GREEN, length=2)


def one_car_game_horizontal():
    car_x_entry = PuzzleEntry(car_x, Orientation.HORIZONTAL, 9)
    puzzle_card = PuzzleCard([car_x_entry])
    return Game(puzzle_card=puzzle_card)


def one_car_game_vertical():
    car_x_entry = PuzzleEntry(car_x, Orientation.VERTICAL, 9)
    puzzle_card = PuzzleCard([car_x_entry])
    return Game(puzzle_card=puzzle_card)


def two_car_game() -> Game:
    car_x_entry = PuzzleEntry(car_x, Orientation.HORIZONTAL, 14)
    car_a_entry = PuzzleEntry(car_a, Orientation.HORIZONTAL, 6)
    puzzle_card = PuzzleCard([car_x_entry, car_a_entry])
    return Game(puzzle_card=puzzle_card)


def three_car_game() -> Game:

    car_x_entry = PuzzleEntry(car_x, Orientation.HORIZONTAL, 14)
    car_a_entry = PuzzleEntry(car_a, Orientation.VERTICAL, 6)
    car_b_entry = PuzzleEntry(car_b, Orientation.VERTICAL, 3)
    puzzle_card = PuzzleCard([car_x_entry, car_a_entry, car_b_entry])
    return Game(puzzle_card=puzzle_card)


def red_car_exit_game() -> Game:
    car_x_entry = PuzzleEntry(car_x, Orientation.HORIZONTAL, 17)
    puzzle_card = PuzzleCard([car_x_entry])
    return Game(puzzle_card=puzzle_card)


def green_car_exit_game() -> Game:
    car_x_entry = PuzzleEntry(car_x, Orientation.HORIZONTAL, 1)
    car_b_entry = PuzzleEntry(car_b, Orientation.HORIZONTAL, 17)
    puzzle_card = PuzzleCard([car_x_entry, car_b_entry])
    return Game(puzzle_card=puzzle_card)


def test_valid_move_right_from_square_nine():
    g = one_car_game_horizontal()
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.RIGHT))
    assert is_valid
    assert new_placement.coverage == [10, 11]


def test_valid_move_left_from_square_nine():
    g = one_car_game_horizontal()
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.LEFT))
    assert is_valid
    assert new_placement.coverage == [8, 9]


def test_invalid_move_up_from_square_nine():
    g = one_car_game_horizontal()
    car_x_placement = g.get_vehicle_placement_for_car(car_x)
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.UP))
    assert not is_valid
    assert new_placement.coverage == car_x_placement.coverage


def test_invalid_move_down_from_square_nine():
    g = one_car_game_horizontal()
    car_x_placement = g.get_vehicle_placement_for_car(car_x)
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.DOWN))
    assert not is_valid
    assert new_placement.coverage == car_x_placement.coverage


def test_valid_move_down_from_square_nine():
    g = one_car_game_vertical()
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.DOWN))
    assert is_valid
    assert new_placement.coverage == [15, 21]


def test_valid_move_up_from_square_nine():
    g = one_car_game_vertical()
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.UP))
    assert is_valid
    assert new_placement.coverage == [3, 9]


def test_invalid_move_right_from_square_nine():
    g = one_car_game_vertical()
    car_x_placement = g.get_vehicle_placement_for_car(car_x)
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.RIGHT))
    assert not is_valid
    assert new_placement.coverage == car_x_placement.coverage


def test_invalid_move_left_from_square_nine():
    g = one_car_game_vertical()
    car_x_placement = g.get_vehicle_placement_for_car(car_x)
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.LEFT))
    assert not is_valid
    assert new_placement.coverage == car_x_placement.coverage


def test_valid_move_down_from_square_six():
    g = three_car_game()
    is_valid, new_placement = g.move(Move(car_a, direction=Direction.DOWN))
    assert is_valid
    assert new_placement.coverage == [12, 18, 24]


def test_invalid_move_left_from_square_three():
    g = three_car_game()
    car_b_placement = g.get_vehicle_placement_for_car(car_b)
    is_valid, new_placement = g.move(Move(car_b, direction=Direction.LEFT))
    assert not is_valid
    assert new_placement.coverage == car_b_placement.coverage


def test_invalid_move_right_from_square_three():
    g = three_car_game()
    car_b_placement = g.get_vehicle_placement_for_car(car_b)
    is_valid, new_placement = g.move(Move(car_b, direction=Direction.RIGHT))
    assert not is_valid
    assert new_placement.coverage == car_b_placement.coverage


def test_invalid_move_down_from_square_twenty_seven():
    g = one_car_game_vertical()
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.DOWN))
    assert is_valid
    assert new_placement.coverage[0] == 15
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.DOWN))
    assert is_valid
    assert new_placement.coverage[0] == 21
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.DOWN))
    assert is_valid
    assert new_placement.coverage[0] == 27
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.DOWN))
    assert not is_valid
    assert new_placement.coverage[0] == 27


def test_vertical_collision():
    g = three_car_game()
    car_b_placement = g.get_vehicle_placement_for_car(car_b)
    is_valid, new_placement = g.move(Move(car_b, direction=Direction.DOWN))
    assert not is_valid
    assert new_placement.coverage == car_b_placement.coverage


def test_horizontal_collision():
    g = three_car_game()
    g.move(Move(car_x, direction=Direction.RIGHT))
    g.move(Move(car_x, direction=Direction.RIGHT))
    car_x_placement = g.get_vehicle_placement_for_car(car_x)
    is_valid, new_placement = g.move(Move(car_x, direction=Direction.RIGHT))
    assert not is_valid
    assert new_placement.coverage == car_x_placement.coverage


def test_three_car_coverage():
    g = three_car_game()
    assert g
    assert g.vehicle_placements
    assert len(g.vehicle_placements) == 3
    covered_squares = sorted(g.calculate_vehicle_placement_coverage_for_all())
    assert [3, 6, 9, 12, 14, 15, 18] == covered_squares


def test_other_car_coverage():
    g = three_car_game()
    assert g
    covered_squares = sorted(g.calculate_vehicle_placement_coverage_for_others(car_x))
    assert [3, 6, 9, 12, 18] == covered_squares


def test_red_car_coverage():
    g = three_car_game()
    assert g
    covered_squares = sorted(g.get_vehicle_placement_for_car(car_x).coverage)
    assert [14, 15] == covered_squares


def test_red_car_can_exit():
    g = red_car_exit_game()
    assert not g.is_puzzle_solved
    is_valid, _ = g.move(Move(car_x, direction=Direction.RIGHT))
    assert is_valid
    assert g.is_puzzle_solved


def test_green_car_can_not_exit():
    g = green_car_exit_game()
    assert not g.is_puzzle_solved
    is_valid, _ = g.move(Move(car_b, direction=Direction.RIGHT))
    assert not is_valid
    assert not g.is_puzzle_solved


def test_parse_card_one_puzzle():

    input_string = "XR2H14,AG2H01,BO2V25,CB2H29,PP3V07,QB3V10,OY3V06,RG3H33"
    card = build_puzzle_card_from_definition(input_string)
    assert card
    assert len(card.puzzle_entries) == 8
    g = Game(card)
    assert len(g.vehicle_placements) == 8
