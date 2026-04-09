from app.application.get_dice_roll import get_dice_roll

EXPECTED_DICE_COUNT = 3
VALID_DICE_VALUES = {1, 2, 3, 4, 5, 6}


def test_result_is_a_valid_dice_value() -> None:
    for _ in range(100):
        result = get_dice_roll()
        assert isinstance(result, list)
        assert len(result) == EXPECTED_DICE_COUNT
        assert all(die in VALID_DICE_VALUES for die in result)
