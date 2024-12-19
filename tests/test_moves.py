# import pytest
from app.main import Board


def test_valid_move_from_position_nine():
    b = Board()
    assert b.move_up(9) == 3
    assert b.move_down(9) == 15
    assert b.move_left(9) == 8
    assert b.move_right(9) == 10
