# import pytest
from app.main import Board, Direction


def test_valid_move_from_position_nine():
    b = Board()
    assert b.move_up(9) == 3
    assert b.move_down(9) == 15
    assert b.move_left(9) == 8
    assert b.move_right(9) == 10


def test_invalid_move_from_position_one():
    b = Board()
    assert b.is_valid_move(1, Direction.UP) == False
    assert b.is_valid_move(1, Direction.LEFT) == False


def test_invalid_move_from_position_six():
    b = Board()
    assert b.is_valid_move(6, Direction.UP) == False
    assert b.is_valid_move(6, Direction.RIGHT) == False


def test_invalid_move_from_position_twelve():
    b = Board()
    assert b.is_valid_move(12, Direction.UP) == True
    assert b.is_valid_move(12, Direction.RIGHT) == False


def test_valid_move_from_position_five():
    b = Board()
    assert b.is_valid_move(5, Direction.RIGHT) == True
