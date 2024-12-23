# import pytest
from app.main import Board, Direction, Car, Position, Colour, Orientation


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


def test_car_length_two_horizontal_position_1():
    b = Board()
    position = Position(
        car=Car(identifier="A", colour=Colour.GREEN, length=2),
        orientation=Orientation.HORIZONTAL,
        board_position=1,
    )
    assert [1, 2] == b.calculate_position_coverage(position=position)


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
