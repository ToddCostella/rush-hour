from icecream import ic
from app.main import (
    Board,
    Direction,
    Car,
    VehiclePlacement,
    Color,
    Orientation,
    Game,
    VehicleID,
)


def card_1_game() -> Game:
    placements = [
        VehiclePlacement(
            car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
            orientation=Orientation.HORIZONTAL,
            start_square=1,
        ),
        VehiclePlacement(
            Car(id=VehicleID("B"), color=Color.PURPLE, length=3),
            orientation=Orientation.VERTICAL,
            start_square=7,
        ),
        VehiclePlacement(
            Car(id=VehicleID("X"), color=Color.RED, length=2),
            orientation=Orientation.HORIZONTAL,
            start_square=14,
        ),
        VehiclePlacement(
            Car(id=VehicleID("D"), color=Color.ORANGE, length=2),
            orientation=Orientation.VERTICAL,
            start_square=25,
        ),
        VehiclePlacement(
            Car(id=VehicleID("E"), color=Color.GREEN, length=3),
            orientation=Orientation.HORIZONTAL,
            start_square=33,
        ),
        VehiclePlacement(
            Car(id=VehicleID("F"), color=Color.BLUE, length=3),
            orientation=Orientation.VERTICAL,
            start_square=10,
        ),
        VehiclePlacement(
            Car(id=VehicleID("G"), color=Color.BLUE, length=2),
            orientation=Orientation.HORIZONTAL,
            start_square=29,
        ),
        VehiclePlacement(
            Car(id=VehicleID("H"), color=Color.YELLOW, length=3),
            orientation=Orientation.VERTICAL,
            start_square=6,
        ),
    ]
    return Game(vehicle_placements=placements)


def two_car_game() -> Game:
    placement = [
        VehiclePlacement(
            Car(id=VehicleID("X"), color=Color.RED, length=2),
            orientation=Orientation.HORIZONTAL,
            start_square=14,
        ),
        VehiclePlacement(
            Car(id=VehicleID("A"), color=Color.BLUE, length=3),
            orientation=Orientation.VERTICAL,
            start_square=6,
        ),
    ]
    return Game(vehicle_placements=placement)


def three_car_game() -> Game:
    placement = [
        VehiclePlacement(
            Car(id=VehicleID("X"), color=Color.RED, length=2),
            orientation=Orientation.HORIZONTAL,
            start_square=14,
        ),
        VehiclePlacement(
            Car(id=VehicleID("A"), color=Color.BLUE, length=3),
            orientation=Orientation.VERTICAL,
            start_square=6,
        ),
        VehiclePlacement(
            Car(id=VehicleID("B"), color=Color.GREEN, length=2),
            orientation=Orientation.HORIZONTAL,
            start_square=3,
        ),
    ]
    return Game(vehicle_placements=placement)


def test_valid_move_from_square_five():
    b = Board()
    assert b.is_valid_move(5, Direction.RIGHT) == True


def test_all_directions_from_square_nine():
    b = Board()
    assert b.move_up(9) == 3
    assert b.move_down(9) == 15
    assert b.move_left(9) == 8
    assert b.move_right(9) == 10


def test_move_all_directions_from_square_one():
    b = Board()
    assert b.move_up(1) == 0
    assert b.move_down(1) == 7
    assert b.move_left(1) == 0
    assert b.move_right(1) == 2


def test_move_all_directions_from_square_six():
    b = Board()
    assert b.move_up(6) == 0
    assert b.move_down(6) == 12
    assert b.move_left(6) == 5
    assert b.move_right(6) == 0


def test_move_all_directions_from_square_thirty_one():
    b = Board()
    assert b.move_up(31) == 25
    assert b.move_down(31) == 0
    assert b.move_left(31) == 0
    assert b.move_right(31) == 32


def test_move_all_directions_from_square_thirty_six():
    b = Board()
    assert b.move_up(36) == 30
    assert b.move_down(36) == 0
    assert b.move_left(36) == 35
    assert b.move_right(36) == 0


def test_invalid_move_from_square_one():
    b = Board()
    assert b.is_valid_move(1, Direction.UP) == False
    assert b.is_valid_move(1, Direction.LEFT) == False


def test_invalid_move_from_square_six():
    b = Board()
    assert b.is_valid_move(6, Direction.UP) == False
    assert b.is_valid_move(6, Direction.RIGHT) == False


def test_invalid_move_from_square_thirty_one():
    b = Board()
    assert b.is_valid_move(31, Direction.DOWN) == False
    assert b.is_valid_move(31, Direction.LEFT) == False


def test_invalid_move_from_square_thirty_six():
    b = Board()
    assert b.is_valid_move(36, Direction.DOWN) == False
    assert b.is_valid_move(36, Direction.RIGHT) == False


def test_invalid_move_from_square_twelve():
    b = Board()
    assert b.is_valid_move(12, Direction.UP) == True
    assert b.is_valid_move(12, Direction.RIGHT) == False


def test_car_length_two_horizontal_square_1():
    b = Board()
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.HORIZONTAL,
        start_square=1,
    )
    assert [1, 2] == b.calculate_vehicle_placement_squares(vehicle_placement=placement)


def test_car_length_three_horizontal_square_1():
    b = Board()
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=3),
        orientation=Orientation.HORIZONTAL,
        start_square=1,
    )
    assert [1, 2, 3] == b.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_car_length_two_horizontal_square_31():
    b = Board()
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.HORIZONTAL,
        start_square=31,
    )
    assert [31, 32] == b.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_car_length_two_vertical_square_1():
    b = Board()
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.VERTICAL,
        start_square=1,
    )
    assert [1, 7] == b.calculate_vehicle_placement_squares(vehicle_placement=placement)


def test_car_length_three_vertical_square_1():
    b = Board()
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=3),
        orientation=Orientation.VERTICAL,
        start_square=1,
    )
    assert [1, 7, 13] == b.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_car_length_two_vertical_square_6():
    b = Board()
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.VERTICAL,
        start_square=6,
    )
    assert [6, 12] == b.calculate_vehicle_placement_squares(vehicle_placement=placement)


def test_car_length_three_vertical_square_6():
    b = Board()
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=3),
        orientation=Orientation.VERTICAL,
        start_square=6,
    )
    assert [6, 12, 18] == b.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_two_car_initial_setup():
    g = two_car_game()
    assert g
    assert g.board
    assert g.vehicle_placements
    assert len(g.vehicle_placements) == 2


def test_three_car_coverage():
    g = three_car_game()
    assert g
    assert g.board
    assert g.vehicle_placements
    assert len(g.vehicle_placements) == 3
    covered_squares = sorted(g.calculate_vehicle_placement_coverage_for_all())
    assert [3, 4, 6, 12, 14, 15, 18] == covered_squares


def test_three_car_other_coverage():
    g = three_car_game()
    assert g.get_vehicle_placement_by_identifier(VehicleID("X"))
    other_squares = g.calculate_vehicle_placement_coverage_for_others(VehicleID("X"))
    my_squares = g.get_my_squares_from_board(VehicleID("X"))
    assert set(other_squares).isdisjoint(my_squares)
