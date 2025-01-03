from icecream import ic
from app.main import (
    Direction,
    Car,
    VehiclePlacement,
    Color,
    Orientation,
    Game,
    VehicleID,
    Move,
)

car_x = Car(id=VehicleID("X"), color=Color.RED, length=2)
car_a = Car(id=VehicleID("A"), color=Color.BLUE, length=3)
car_b = Car(id=VehicleID("B"), color=Color.GREEN, length=2)


def two_car_game() -> Game:
    placement = [
        VehiclePlacement(
            car=car_x,
            orientation=Orientation.HORIZONTAL,
            coverage=[14],
        ),
        VehiclePlacement(car=car_a, orientation=Orientation.VERTICAL, coverage=[6]),
    ]
    return Game(vehicle_placements=placement)


def three_car_game() -> Game:
    placement = [
        VehiclePlacement(
            car_x,
            orientation=Orientation.HORIZONTAL,
            coverage=[14],
        ),
        VehiclePlacement(
            car_a,
            orientation=Orientation.VERTICAL,
            coverage=[6],
        ),
        VehiclePlacement(
            car_b,
            orientation=Orientation.HORIZONTAL,
            coverage=[3],
        ),
    ]
    return Game(vehicle_placements=placement)


def test_valid_move_from_square_five():
    g = Game(vehicle_placements=[])
    assert g.is_valid_move(Move(from_position=5, direction=Direction.RIGHT)) == True


def test_all_directions_from_square_nine():
    g = Game(vehicle_placements=[])
    assert g.move_up(9) == 3
    assert g.move_down(9) == 15
    assert g.move_left(9) == 8
    assert g.move_right(9) == 10


def test_move_all_directions_from_square_one():
    g = Game(vehicle_placements=[])
    assert g.move_up(1) == 0
    assert g.move_down(1) == 7
    assert g.move_left(1) == 0
    assert g.move_right(1) == 2


def test_move_all_directions_from_square_six():
    g = Game(vehicle_placements=[])
    assert g.move_up(6) == 0
    assert g.move_down(6) == 12
    assert g.move_left(6) == 5
    assert g.move_right(6) == 0


def test_move_all_directions_from_square_thirty_one():
    g = Game(vehicle_placements=[])
    assert g.move_up(31) == 25
    assert g.move_down(31) == 0
    assert g.move_left(31) == 0
    assert g.move_right(31) == 32


def test_move_all_directions_from_square_thirty_six():
    g = Game(vehicle_placements=[])
    assert g.move_up(36) == 30
    assert g.move_down(36) == 0
    assert g.move_left(36) == 35
    assert g.move_right(36) == 0


def test_invalid_move_from_square_one():
    g = Game(vehicle_placements=[])
    assert g.is_valid_move(Move(from_position=1, direction=Direction.UP)) == False
    assert g.is_valid_move(Move(from_position=1, direction=Direction.LEFT)) == False


def test_invalid_move_from_square_six():
    g = Game(vehicle_placements=[])
    assert g.is_valid_move(Move(from_position=6, direction=Direction.UP)) == False
    assert g.is_valid_move(Move(from_position=6, direction=Direction.RIGHT)) == False


def test_invalid_move_from_square_thirty_one():
    g = Game(vehicle_placements=[])
    assert g.is_valid_move(Move(from_position=31, direction=Direction.DOWN)) == False
    assert g.is_valid_move(Move(from_position=31, direction=Direction.LEFT)) == False


def test_invalid_move_from_square_thirty_six():
    g = Game(vehicle_placements=[])
    assert g.is_valid_move(Move(from_position=36, direction=Direction.DOWN)) == False
    assert g.is_valid_move(Move(from_position=36, direction=Direction.RIGHT)) == False


def test_invalid_move_from_square_twelve():
    g = Game(vehicle_placements=[])
    assert g.is_valid_move(Move(from_position=12, direction=Direction.UP)) == True
    assert g.is_valid_move(Move(from_position=12, direction=Direction.RIGHT)) == False


def test_car_length_two_horizontal_square_1():
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.HORIZONTAL,
        start_square=1,
    )
    g = Game(vehicle_placements=[placement])
    assert [1, 2] == g.calculate_vehicle_placement_squares(vehicle_placement=placement)


def test_car_length_three_horizontal_square_1():
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=3),
        orientation=Orientation.HORIZONTAL,
        start_square=1,
    )
    g = Game(vehicle_placements=[placement])
    assert [1, 2, 3] == g.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_car_length_two_horizontal_square_31():
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.HORIZONTAL,
        start_square=31,
    )
    g = Game(vehicle_placements=[placement])
    assert [31, 32] == g.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_car_length_two_vertical_square_1():
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.VERTICAL,
        start_square=1,
    )
    g = Game(vehicle_placements=[placement])
    assert [1, 7] == g.calculate_vehicle_placement_squares(vehicle_placement=placement)


def test_car_length_three_vertical_square_1():
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=3),
        orientation=Orientation.VERTICAL,
        start_square=1,
    )
    g = Game(vehicle_placements=[placement])
    assert [1, 7, 13] == g.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_car_length_two_vertical_square_6():
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=2),
        orientation=Orientation.VERTICAL,
        start_square=6,
    )
    g = Game(vehicle_placements=[placement])
    assert [6, 12] == g.calculate_vehicle_placement_squares(vehicle_placement=placement)


def test_car_length_three_vertical_square_6():
    placement = VehiclePlacement(
        car=Car(id=VehicleID("A"), color=Color.GREEN, length=3),
        orientation=Orientation.VERTICAL,
        start_square=6,
    )
    g = Game(vehicle_placements=[placement])
    assert [6, 12, 18] == g.calculate_vehicle_placement_squares(
        vehicle_placement=placement
    )


def test_two_car_initial_setup():
    g = two_car_game()
    assert g
    assert g.vehicle_placements
    assert len(g.vehicle_placements) == 2


def test_three_car_coverage():
    g = three_car_game()
    assert g
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
