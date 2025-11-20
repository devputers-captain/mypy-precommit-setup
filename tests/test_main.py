from app.main import calculate_total


def test_calculate_total() -> None:
    assert calculate_total(10.0, 2) == 20.0
