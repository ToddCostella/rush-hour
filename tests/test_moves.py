# import pytest
from app.main import Board, Direction, Car, Position, Colour, Orientation, Game


def card_1_game() -> Game:
    positions = [
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
    return Game(positions=positions)


def simple_two_car_game() -> Game:
    positions = [
        Position(
            Car(identifier="X", colour=Colour.RED, length=2),
            orientation=Orientation.HORIZONTAL,
            board_position=14,
        ),
        Position(
            Car(identifier="A", colour=Colour.BLUE, length=3),
            orientation=Orientation.VERTICAL,
            board_position=6,
        ),
    ]
    return Game(positions=positions)


def test_valid_move_from_position_five():
    b = Board()
    assert b.is_valid_move(5, Direction.RIGHT) == True


def test_all_directions_from_position_nine():
    b = Board()
    assert b.move_up(9) == 3
    assert b.move_down(9) == 15
    assert b.move_left(9) == 8
    assert b.move_right(9) == 10


def test_move_all_directions_from_position_one():
    b = Board()
    assert b.move_up(1) == 0
    assert b.move_down(1) == 7
    assert b.move_left(1) == 0
    assert b.move_right(1) == 2


def test_move_all_directions_from_position_six():
    b = Board()
    assert b.move_up(6) == 0
    assert b.move_down(6) == 12
    assert b.move_left(6) == 5
    assert b.move_right(6) == 0


def test_move_all_directions_from_position_thirty_one():
    b = Board()
    assert b.move_up(31) == 25
    assert b.move_down(31) == 0
    assert b.move_left(31) == 0
    assert b.move_right(31) == 32


def test_move_all_directions_from_position_thirty_six():
    b = Board()
    assert b.move_up(36) == 30
    assert b.move_down(36) == 0
    assert b.move_left(36) == 35
    assert b.move_right(36) == 0


def test_invalid_move_from_position_one():
    b = Board()
    assert b.is_valid_move(1, Direction.UP) == False
    assert b.is_valid_move(1, Direction.LEFT) == False


def test_invalid_move_from_position_six():
    b = Board()
    assert b.is_valid_move(6, Direction.UP) == False
    assert b.is_valid_move(6, Direction.RIGHT) == False


def test_invalid_move_from_position_thirty_one():
    b = Board()
    assert b.is_valid_move(31, Direction.DOWN) == False
    assert b.is_valid_move(31, Direction.LEFT) == False


def test_invalid_move_from_position_thirty_six():
    b = Board()
    assert b.is_valid_move(36, Direction.DOWN) == False
    assert b.is_valid_move(36, Direction.RIGHT) == False


def test_invalid_move_from_position_twelve():
    b = Board()
    assert b.is_valid_move(12, Direction.UP) == True
    assert b.is_valid_move(12, Direction.RIGHT) == False


def test_car_length_two_horizontal_position_1():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=2),
        orientation=Orientation.HORIZONTAL,
        board_position=1,
    )
    assert [1, 2] == b.calculate_position_coverage(position=position)


def test_car_length_three_horizontal_position_1():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=3),
        orientation=Orientation.HORIZONTAL,
        board_position=1,
    )
    assert [1, 2, 3] == b.calculate_position_coverage(position=position)


def test_car_length_two_horizontal_position_31():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=2),
        orientation=Orientation.HORIZONTAL,
        board_position=31,
    )
    assert [31, 32] == b.calculate_position_coverage(position=position)


def test_car_length_two_vertical_position_1():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=2),
        orientation=Orientation.VERTICAL,
        board_position=1,
    )
    assert [1, 7] == b.calculate_position_coverage(position=position)


def test_car_length_three_vertical_position_1():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=3),
        orientation=Orientation.VERTICAL,
        board_position=1,
    )
    assert [1, 7, 13] == b.calculate_position_coverage(position=position)


def test_car_length_two_vertical_position_6():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=2),
        orientation=Orientation.VERTICAL,
        board_position=6,
    )
    assert [6, 12] == b.calculate_position_coverage(position=position)


def test_car_length_three_vertical_position_6():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=3),
        orientation=Orientation.VERTICAL,
        board_position=6,
    )
    assert [6, 12, 18] == b.calculate_position_coverage(position=position)


def test_simple_game_initial_setup():
    g = simple_two_car_game()
    assert g
    assert g.board
    assert g.positions
    assert len(g.positions) == 2


def test_find_car_x():
    g = simple_two_car_game()
    car_x = g.get_car_by_id("X")
    assert car_x
    assert car_x.colour == Colour.RED


def test_find_car_z_should_fail():
    g = simple_two_car_game()
    _ = g.get_car_by_id("Z")
    assert _ is None


def test_simple_game_other_car_coverage():
    g = simple_two_car_game()
    board = g.board
